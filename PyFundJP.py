#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5

import urllib.request
import pandas as pd
import datetime
import lxml.html


class PyFundJP():
    def __init__(self, isin):
        self.isin = isin

    # 属性を取得する
    def detail(self):
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

        f = lambda t: t.text.replace('\n','')
        labels_top = list(map(f, labels_top))
        labels_mid = list(map(f, labels_mid))
        labels_bottom = list(map(f, labels_bottom))

        # 空dictに値をセット
        d = dict()

        d['isin_cd'] = self.isin
        d['closing_date'] = labels_top[0]
        d['index_type'] = labels_top[1]
        d['trustee_fee'] = labels_top[2]
        d['unit_type'] = labels_top[3]
        d['establishment_date'] = labels_top[4]
        d['fund_ctg1'] = labels_top[5]
        d['fund_ctg2'] = labels_top[6]
        d['fund_name'] = labels_top[7]
        d['fund_shortname'] = labels_top[8]
        d['asset_manager'] = labels_top[9]

        d['independent_division'] = labels_mid[0]
        d['investment_asset'] = labels_mid[1]
        d['investment_style'] = labels_mid[2]
        d['establishment_date2'] = labels_mid[3]
        d['close_date'] = labels_mid[4]

        d['trustee_fee_am'] = labels_bottom[0]
        # 無報酬の場合は'buying_fee'が取れず要素数が5になる
        if len(labels_bottom) == 5:
            d['buying_fee'] = 0
            d['partical_redemption_charge'] = labels_bottom[1]
            d['trustee_fee2'] = labels_bottom[2]
            d['trustee_fee_seller'] = labels_bottom[3]
            d['trustee_fee_custody'] = labels_bottom[4]
        else:
            d['buying_fee'] = labels_bottom[1]
            d['partical_redemption_charge'] = labels_bottom[2]
            d['trustee_fee2'] = labels_bottom[3]
            d['trustee_fee_seller'] = labels_bottom[4]
            d['trustee_fee_custody'] = labels_bottom[5]

        return d

    # 基準価格を取得する
    def nav(self, sy, sm, sd, ey, em ,ed):
        # 取得開始日,取得終了日,設定日を取得
        d = dict()
        d['from'] = datetime.date(sy, sm, sd)
        d['to'] = datetime.date(ey, em, ed)

        detail = self.detail()
        d['est'] = datetime.datetime.strptime(detail['establishment_date'], '%Y/%m/%d').date()

        # 初期期間
        d['start'] = max([d['from'], d['est']])
        d['end'] = d['start'] + datetime.timedelta(days=90)

        df_res = pd.DataFrame({})

        loop_flg = True
        while loop_flg:
            # 取得期間の終端が終期を超える場合は終端に合わせる
            if d['end'] >= d['to']:
                d['end'] = d['to']
                loop_flg = False

            # 取得処理
            k = ['sy', 'sm', 'sd', 'ey', 'em', 'ed']
            v = [d['start'].year, d['start'].month, d['start'].day, d['end'].year, d['end'].month, d['end'].day]
            v = list(map(lambda s:str(s).zfill(2), v))

            args = dict(zip(k, v))
            args['isinCd'] = self.isin

            # URL生成
            url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030004.seam?isinCd={isinCd}\
&stdDateFromY={sy}&stdDateFromM={sm}&stdDateFromD={sd}\
&stdDateToY={ey}&stdDateToM={em}&stdDateToD={ed}&showFlg=csv&adminFlag=2'.format(**args)
            response = urllib.request.urlopen(url)

            try:
                df = pd.read_csv(response, encoding='Shift_JIS', index_col=0)
            except:
                df = pd.DataFrame({})

            df_res = df_res.append(df)

            # 取得開始日を取得終了日の翌日にする
            d['start'] = d['end'] + datetime.timedelta(days=1)
            d['end'] = d['start'] + datetime.timedelta(days=90)

        return df_res
