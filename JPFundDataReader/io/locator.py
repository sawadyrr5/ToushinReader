#!/usr/local/bin python
# -*- coding: UTF-8 -*-
class BaseLocator(object):
    url = None
    xpath = None

    @property
    def url(self):
        return self.url

    @property
    def xpath(self):
        return self.xpath


class AttributeLocator(BaseLocator):
    url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030000.seam?isinCd={isinCd}'
    xpath = {
        '決算頻度': '//*[@id="contents"]/div[2]/div/table[1]//tr[2]/td[1]/label',
        'インデックス型': '//*[@id="contents"]/div[2]/div/table[1]//tr[2]/td[2]/label',
        '信託報酬': '//*[@id="contents"]/div[2]/div/table[1]//tr[2]/td[3]/label',
        '単位型・追加型': '//*[@id="contents"]/div[2]/div/table[1]//tr[2]/td[4]/label',
        '設定日': '//*[@id="contents"]/div[2]/div/table[1]//tr[2]/td[5]/label',

        '大分類': '//*[@id="contents"]/div[2]/div/table[1]//tr[3]/td[1]/strong/label[1]',
        '中分類': '//*[@id="contents"]/div[2]/div/table[1]//tr[3]/td[1]/strong/label[2]',
        'ファンド名称': '//*[@id="contents"]/div[2]/div/table[1]//tr[3]/td[2]/strong[1]/label',
        'ファンド略称': '//*[@id="contents"]/div[2]/div/table[1]//tr[3]/td[2]/strong[2]/label',
        '運用会社': '//*[@id="contents"]/div[2]/div/table[1]//tr[3]/td[2]/label',

        '独立区分': '//*[@id="contents"]/div[2]/div/table[3]//tr[2]/td[1]/label',
        '投資対象資産': '//*[@id="contents"]/div[2]/div/table[3]//tr[2]/td[2]/label',
        '資産属性': '//*[@id="contents"]/div[2]/div/table[3]//tr[2]/td[3]',
        '投資形態': '//*[@id="contents"]/div[2]/div/table[3]//tr[2]/td[4]/label',
        '償還日': '//*[@id="contents"]/div[2]/div/table[3]//tr[2]/td[6]/label'
    }


class AttributeFundLocator(AttributeLocator):
    def __init__(self):
        self.xpath.update(
            {
                '購入時手数料・上限（税抜）': '//*[@id="contents"]/div[4]/div[1]/table[1]//tr[2]/th[1]/label',
                '信託財産留保額': '//*[@id="contents"]/div[4]/div[1]/table//tr[2]/th[2]/label',
                '信託報酬_委託会社': '//*[@id="contents"]/div[4]/div[1]/table//tr[1]/th[9]/label',
                '信託報酬_販売会社': '//*[@id="contents"]/div[4]/div[1]/table//tr[2]/th[5]/label',
                '信託報酬_受託会社': '//*[@id="contents"]/div[4]/div[1]/table[1]//tr[3]/th[2]/label'
            }
        )


class AttributeMRFLocator(AttributeLocator):
    def __init__(self):
        self.xpath.update(
            {
                '購入時手数料・上限（税抜）': '//*[@id="contents"]/div[3]/div[1]/table[1]//tr[2]/th[1]/label',
                '信託財産留保額': '//*[@id="contents"]/div[3]/div[1]/table//tr[2]/th[2]/label',
                '信託報酬_委託会社': '//*[@id="contents"]/div[3]/div[1]/table//tr[1]/th[9]/label',
                '信託報酬_販売会社': '//*[@id="contents"]/div[3]/div[1]/table//tr[2]/th[5]/label',
                '信託報酬_受託会社': '//*[@id="contents"]/div[3]/div[1]/table[1]//tr[3]/th[2]/label'
            }
        )


class NAVLocator(BaseLocator):
    url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030004.seam?isinCd={isinCd}&' \
          'stdDateFromY={sy}&stdDateFromM={sm}&stdDateFromD={sd}&' \
          'stdDateToY={ey}&stdDateToM={em}&stdDateToD={ed}&showFlg=csv&adminFlag=2'


class ReturnLocator(BaseLocator):
    url = 'http://tskl.toushin.or.jp/FdsWeb/view/FDST030002.seam?isinCd={isinCd}&' \
          'initFlag=1&stdDateFromY={sy}&stdDateFromM={sm}&stdDateFromD={sd}&' \
          'stdDateToY={ey}&stdDateToM={em}&stdDateToD={ed}&buyAmntMoney={buyAmntMoney}'
    xpath = {
        '騰落率（分配金込）（購入額当り）': {
            '所有期間損益': '//*[@id="showList"]/table[2]//tr[2]/td[1]',
            '分配金累計': '//*[@id="showList"]/table[2]//tr[2]/td[2]',
            '所有期間損益（分配金含む）': '//*[@id="showList"]/table[2]//tr[2]/td[3]',
            '収益率': '//*[@id="showList"]/table[2]//tr[2]/td[4]'
        },
        '騰落率（分配金込）（一口当り）': {
            '所有期間損益': '//*[@id="showList"]/table[2]//tr[3]/td[1]',
            '分配金累計': '//*[@id="showList"]/table[2]//tr[3]/td[2]',
            '所有期間損益（分配金含む）': '//*[@id="showList"]/table[2]//tr[3]/td[3]',
            '収益率': '//*[@id="showList"]/table[2]//tr[3]/td[4]'
        }
    }


class ReturnPerAmountLocator(ReturnLocator):
    xpath = {
        '所有期間損益': '//*[@id="showList"]/table[2]/tbody/tr[2]/td[1]',
        '分配金累計': '//*[@id="showList"]/table[2]/tbody/tr[2]/td[2]',
        '所有期間損益（分配金含む）': '//*[@id="showList"]/table[2]/tbody/tr[2]/td[3]',
        '収益率': '//*[@id="showList"]/table[2]/tbody/tr[2]/td[4]'
    }


class ReturnPerShareLocator(ReturnLocator):
    xpath = {
        '所有期間損益': '//*[@id="showList"]/table[2]//tr[3]/td[1]',
        '分配金累計': '//*[@id="showList"]/table[2]//tr[3]/td[2]',
        '所有期間損益（分配金含む）': '//*[@id="showList"]/table[2]//tr[3]/td[3]',
        '収益率': '//*[@id="showList"]/table[2]//tr[3]/td[4]'
    }
