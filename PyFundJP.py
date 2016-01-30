#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
import urllib.request
import pandas as pd
import datetime
import lxml.html
from decimal import *


class PyFundJP:
    def __init__(self, isin):
        self.isin = isin

        getcontext().prec = 15

    # 属性を取得する
    def attrib(self):
        # URL生成
        args = dict(isinCd=self.isin)
        url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030000.seam?isinCd={isinCd}'.format(**args)

        html = urllib.request.urlopen(url).read()
        root = lxml.html.fromstring(html)

        xpath_top = '//*[@id="contents"]/div[2]/div/table[1]//label'
        xpath_mid = '//*[@id="contents"]/div[2]/div/table[3]//label'
        xpath_bottom = '//*[@id="contents"]//table[@class="dividend"]//label'

        labels_top = root.xpath(xpath_top)
        labels_mid = root.xpath(xpath_mid)
        labels_bottom = root.xpath(xpath_bottom)

        f = lambda t: t.text.replace('\n', '')
        labels_top = list(map(f, labels_top))
        labels_mid = list(map(f, labels_mid))
        labels_bottom = list(map(f, labels_bottom))

        # 空dictに値をセット
        attrib = dict()

        attrib['isin_cd'] = self.isin
        attrib['closing_date'] = labels_top[0]          # 決算日
        attrib['index_type'] = labels_top[1]            # インデックス型
        attrib['trustee_fee'] = labels_top[2]           # 信託報酬
        attrib['unit_type'] = labels_top[3]             # 単位型、追加型
        attrib['establishment_date'] = labels_top[4]    # 設定日
        attrib['fund_ctg1'] = labels_top[5]             # カテゴリ1
        attrib['fund_ctg2'] = labels_top[6]             # カテゴリ2
        attrib['fund_name'] = labels_top[7]             # ファンド名
        attrib['fund_shortname'] = labels_top[8]        # ファンド略名
        attrib['asset_manager'] = labels_top[9]         # 委託会社

        attrib['independent_division'] = labels_mid[0]  # 独立区分
        attrib['investment_asset'] = labels_mid[1]      # 投資対象資産
        attrib['investment_style'] = labels_mid[2]      # 資産属性
        attrib['establishment_date2'] = labels_mid[3]   # 設定日2
        attrib['close_date'] = labels_mid[4]            # 償還日

        attrib['trustee_fee_am'] = labels_bottom[0]     # 信託報酬(委託)
        # 無報酬の場合は'buying_fee'が取れず要素数が5になる
        if len(labels_bottom) == 5:
            attrib['buying_fee'] = 0                    # 購入手数料
            attrib['partical_redemption_charge'] = labels_bottom[1]     # 信託財産留保金
            attrib['trustee_fee2'] = labels_bottom[2]                   # 信託報酬その2
            attrib['trustee_fee_seller'] = labels_bottom[3]             # 信託報酬(販売)
            attrib['trustee_fee_custody'] = labels_bottom[4]            # 信託報酬(受託)
        else:
            attrib['buying_fee'] = labels_bottom[1]
            attrib['partical_redemption_charge'] = labels_bottom[2]
            attrib['trustee_fee2'] = labels_bottom[3]
            attrib['trustee_fee_seller'] = labels_bottom[4]
            attrib['trustee_fee_custody'] = labels_bottom[5]

        return attrib

    # 基準価格を取得する
    def nav(self, date_from, date_to):
        # 期間開始日, 期間終了日を設定
        d = dict()
        d['from'] = datetime.datetime.strptime(date_from, '%Y-%m-%d').date()
        d['to'] = datetime.datetime.strptime(date_to, '%Y-%m-%d').date()

        # 設定日を設定
        attrib = self.attrib()
        d['est'] = datetime.datetime.strptime(attrib['establishment_date'], '%Y/%m/%d').date()

        # 期間開始日と設定日の大きい方を取得開始日とする
        d['start'] = max([d['from'], d['est']])
        d['end'] = d['start'] + datetime.timedelta(days=90)

        df_res = pd.DataFrame({})

        loop_flg = True
        while loop_flg:
            # 取得終了日が期間終了日を超える場合は期間終了日を取得終了日とする
            if d['end'] >= d['to']:
                d['end'] = d['to']
                loop_flg = False

            # URL生成
            k = ['sy', 'sm', 'sd', 'ey', 'em', 'ed']
            v = [d['start'].year, d['start'].month, d['start'].day, d['end'].year, d['end'].month, d['end'].day]
            v = list(map(lambda s: str(s).zfill(2), v))
            args = dict(zip(k, v))
            args['isinCd'] = self.isin

            url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030004.seam?isinCd={isinCd}\
&stdDateFromY={sy}&stdDateFromM={sm}&stdDateFromD={sd}\
&stdDateToY={ey}&stdDateToM={em}&stdDateToD={ed}&showFlg=csv&adminFlag=2'.format(**args)
            response = urllib.request.urlopen(url)

            # データを取得しDataFrameに追加
            try:
                df = pd.read_csv(response, encoding='Shift_JIS', index_col=0)
            except ValueError:
                df = pd.DataFrame({})

            df_res = df_res.append(df)

            # 取得終了日の翌日を次の取得開始日にする
            d['start'] = d['end'] + datetime.timedelta(days=1)
            d['end'] = d['start'] + datetime.timedelta(days=90)

        return df_res

    # 騰落率を取得する
    def perf(self, date_from, date_to, amount_money):
        # 期間開始日, 期間終了日を設定
        d = dict()
        d['from'] = datetime.datetime.strptime(date_from, '%Y-%m-%d').date()
        d['to'] = datetime.datetime.strptime(date_to, '%Y-%m-%d').date()

        # URL生成
        k = ['sy', 'sm', 'sd', 'ey', 'em', 'ed']
        v = [d['from'].year, d['from'].month, d['from'].day, d['to'].year, d['to'].month, d['to'].day]
        v = list(map(lambda s: str(s).zfill(2), v))
        args = dict(zip(k, v))
        args['isinCd'] = self.isin
        args['buyAmntMoney'] = amount_money

        url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030002.seam?isinCd={isinCd}&initFlag=1&\
stdDateFromY={sy}&stdDateFromM={sm}&stdDateFromD={sd}&\
stdDateToY={ey}&stdDateToM={em}&stdDateToD={ed}&buyAmntMoney={buyAmntMoney}'.format(**args)

        html = urllib.request.urlopen(url).read()
        root = lxml.html.fromstring(html)

        xpath = '//div[@id="showList"]/table[2]/tr[2]//td'
        contents = root.xpath(xpath)

        # 所有期間損益, 分配金累計, 所有期間損益（分配金含む）, 収益率(年換算)
        f = lambda elem: Decimal(elem.text_content().replace(',', '').replace('円', ''))

        try:
            k = ['pl', 'dividend_total', 'pl_include_dividend', 'return']
            v = list(map(f, [contents[0], contents[1], contents[2]]))
            v.append(Decimal(contents[3].text_content().replace('\n', '').replace('%', '')) / 100)
            perf = dict(zip(k, v))

        except IndexError:
            perf = dict()

        return perf
