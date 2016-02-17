#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
import urllib.request
import pandas as pd
from datetime import datetime, timedelta
import lxml.html
import decimal


class PyFundJP:
    """
    Pythonで日本国内の投資信託関連情報を取得するクラス
    """
    def __init__(self, isin, start, end):
        self.isin = isin
        self.start = start
        self.end = end
        decimal.getcontext().prec = 15

    def attrib(self):
        """
        Get fund attribute
        :return:
        """
        args = dict(isinCd=self.isin)
        url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030000.seam?isinCd={isinCd}'.format(**args)

        html = urllib.request.urlopen(url).read()
        root = lxml.html.fromstring(html)

        xpaths = ('//*[@id="contents"]/div[2]/div/table[1]//label',
                  '//*[@id="contents"]/div[2]/div/table[3]//label',
                  '//*[@id="contents"]//table[@class="dividend"]//label')

        labels = [root.xpath(x) for x in xpaths]
        labels = [[t.text.replace('\n', '') for t in l] for l in labels]

        attrib = dict()
        attrib['isin_cd'] = self.isin
        attrib['closing_date'] = labels[0][0]                       # 決算日
        attrib['index_type'] = labels[0][1]                         # インデックス型
        attrib['trustee_fee'] = labels[0][2]                        # 信託報酬
        attrib['unit_type'] = labels[0][3]                          # 単位型、追加型
        attrib['establishment_date'] = labels[0][4]                 # 設定日
        attrib['fund_ctg1'] = labels[0][5]                          # カテゴリ1
        attrib['fund_ctg2'] = labels[0][6]                          # カテゴリ2
        attrib['fund_name'] = labels[0][7]                          # ファンド名
        attrib['fund_shortname'] = labels[0][8]                     # ファンド略名
        attrib['asset_manager'] = labels[0][9]                      # 委託会社

        attrib['independent_division'] = labels[1][0]               # 独立区分
        attrib['investment_asset'] = labels[1][1]                   # 投資対象資産
        attrib['investment_style'] = labels[1][2]                   # 資産属性
        attrib['establishment_date2'] = labels[1][3]                # 設定日2
        attrib['close_date'] = labels[1][4]                         # 償還日

        attrib['trustee_fee_am'] = labels[2][0]                     # 信託報酬(委託)
        # 無報酬の場合は'buying_fee'が取れず要素数が5になる
        if len(labels[2]) == 5:
            attrib['buying_fee'] = 0                                # 購入手数料
            attrib['partical_redemption_charge'] = labels[2][1]     # 信託財産留保金
            attrib['trustee_fee2'] = labels[2][2]                   # 信託報酬その2
            attrib['trustee_fee_seller'] = labels[2][3]             # 信託報酬(販売)
            attrib['trustee_fee_custody'] = labels[2][4]            # 信託報酬(受託)
        else:
            attrib['buying_fee'] = labels[2][1]
            attrib['partical_redemption_charge'] = labels[2][2]
            attrib['trustee_fee2'] = labels[2][3]
            attrib['trustee_fee_seller'] = labels[2][4]
            attrib['trustee_fee_custody'] = labels[2][5]

        return attrib

    # 基準価格を取得する
    def nav(self):
        """
        :return:
        pandas.DataFrame

        Index
            Date
        Columns
            NAV
            Capital
            Dividend
            Closing
        """
        date_est = datetime.strptime(self.attrib()['establishment_date'], '%Y/%m/%d')
        date_from = max([self.start, date_est])

        baseurl = ('http://tskl.toushin.or.jp/FdsWeb/view/FDST030004.seam?isinCd={isinCd}'
               '&stdDateFromY={sy}&stdDateFromM={sm}&stdDateFromD={sd}&stdDateToY={ey}'
               '&stdDateToM={em}&stdDateToD={ed}&showFlg=csv&adminFlag=2')

        df_res = pd.DataFrame()
        while True:
            date_to = date_from + timedelta(days=90)
            if date_to > self.end:
                date_to = self.end

            k = ['sy', 'sm', 'sd', 'ey', 'em', 'ed']
            v = [date_from.year, date_from.month, date_from.day, date_to.year, date_to.month, date_to.day]
            v = [str(s).zfill(2) for s in v]
            args = dict(zip(k, v))
            args['isinCd'] = self.isin

            url = baseurl.format(**args)
            response = urllib.request.urlopen(url)

            try:
                df = pd.read_csv(response, encoding='Shift_JIS')
            except ValueError:
                df = pd.DataFrame()
            df_res = df_res.append(df)

            date_from = date_to + timedelta(days=1)
            if date_from > self.end:
                break

        df_res.columns = ('Date', 'NAV', 'Capital', 'Dividend', 'Closing')
        df_res['Date'] = df_res['Date'].apply(lambda s: pd.to_datetime(s, format=u'%Y年%m月%d日'))
        df_res.set_index('Date')

        return df_res

    def perf(self, amount_money):
        """
        騰落率を取得する

        :param amount_money:
        :return:

        pl                      所有期間損益
        dividend_total          分配金累計
        pl_include_dividend     所有期間損益（分配金含む）
        return                  収益率(年換算)
        """
        k = ['sy', 'sm', 'sd', 'ey', 'em', 'ed']
        v = [self.start.year, self.start.month, self.start.day, self.end.year, self.end.month, self.end.day]
        v = [str(s).zfill(2) for s in v]
        args = dict(zip(k, v))
        args['isinCd'] = self.isin
        args['buyAmntMoney'] = amount_money

        url = ('http://tskl.toushin.or.jp/FdsWeb/view/FDST030002.seam?isinCd={isinCd}&'
               'initFlag=1&stdDateFromY={sy}&stdDateFromM={sm}&stdDateFromD={sd}&'
               'stdDateToY={ey}&stdDateToM={em}&stdDateToD={ed}&buyAmntMoney={buyAmntMoney}').format(**args)

        html = urllib.request.urlopen(url).read()
        root = lxml.html.fromstring(html)

        xpath = '//div[@id="showList"]/table[2]/tr[2]//td'
        contents = root.xpath(xpath)

        # 所有期間損益, 分配金累計, 所有期間損益（分配金含む）, 収益率(年換算)
        try:
            f = lambda elem: decimal.Decimal(elem.text_content().replace(',', '').replace('円', ''))
            k = ['pl', 'dividend_total', 'pl_include_dividend', 'return']
            v = list(map(f, [contents[0], contents[1], contents[2]]))
            v.append(decimal.Decimal(contents[3].text_content().replace('\n', '').replace('%', '')) / 100)
            perf = dict(zip(k, v))
        except IndexError:
            perf = dict()

        return perf


if __name__ == '__main__':
    ISIN = 'JP90C000A931'                           # 日本株アルファ・カルテット（毎月分配型）
    start = datetime(2015, 1, 1)
    end = datetime(2015, 12, 31)

    myFund = PyFundJP(ISIN, start, end)
    print(myFund.attrib())
    print(myFund.nav())
    print(myFund.perf(1000000))
