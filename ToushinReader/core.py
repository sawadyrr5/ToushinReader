# -*- coding: utf-8 -*-
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from requests import Session
from bs4 import BeautifulSoup
from ToushinReader.locator import AttributeLocator

disable_warnings(InsecureRequestWarning)


class Fund:
    def __init__(self, isin_code: str):
        url = f"https://toushin-lib.fwg.ne.jp/FdsWeb/FDST030000?isinCd={isin_code}"

        self._soup = BeautifulSoup(
            Session().get(url, verify=False).text, features="html.parser"
        )

    def _parse_element(self, css_selector: str, attr: str = None) -> str:

        res = [elem.get(attr) if attr else elem.text for elem in self._soup.select(css_selector)]

        if len(res) > 0:
            return str(res[0])

    @staticmethod
    def _sanitize(text: str) -> str:
        if text:
            res = (
                text.replace("評価基準日\xa0\xa0", "")
                    .replace("愛称：", "")
                    .replace("運用会社名：", "")
                    .replace("\n", "")
                    .strip()
            )

            return res

    @property
    def as_of_date(self) -> str:
        """
        評価基準日
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.AS_OF_DATE))

    @property
    def name(self) -> str:
        """
        ファンド名
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.FUND_NAME))

    @property
    def nickname(self) -> str:
        """
        愛称
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.FUND_NICKNAME))

    @property
    def investment_manager(self) -> str:
        """
        運用会社名
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.INVESTMENT_MANAGER))

    @property
    def basic_price(self) -> str:
        """
        基準価額
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.BASIC_PRICE))

    @property
    def basic_price_yen_positive_change(self) -> str:
        """
        基準価額前日比変化幅(上昇)
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.BASIC_PRICE_YEN_POSITIVE_CHANGE))

    @property
    def basic_price_pct_positive_change(self) -> str:
        """
        基準価額前日比変化率(上昇)
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.BASIC_PRICE_PCT_POSITIVE_CHANGE))

    @property
    def basic_price_yen_negaitive_change(self) -> str:
        """
        基準価額前日比変化幅(下落)
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.BASIC_PRICE_YEN_NEGATIVE_CHANGE))

    @property
    def basic_price_pct_negative_change(self) -> str:
        """
        基準価額前日比変化率(下落)
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.BASIC_PRICE_PCT_NEGATIVE_CHANGE))

    @property
    def net_asset_amount(self) -> str:
        """
        純資産総額
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.NET_ASSET_AMOUNT))

    @property
    def category(self) -> str:
        """
        商品分類
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.CATEGORY))

    @property
    def index_type(self) -> str:
        """
        インデックス型
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.INDEX_TYPE))

    @property
    def establish_date(self) -> str:
        """
        設定日
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.ESTABLISH_DATE))

    @property
    def closing_date(self) -> str:
        """
        償還日
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.CLOSING_DATE))

    @property
    def date_to_closing(self) -> str:
        """
        償還までの期間
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.DATE_TO_CLOSING))

    @property
    def settlement_freq(self) -> str:
        """
        決算頻度
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.SETTLEMENT_FREQ))

    @property
    def date_of_settlement(self) -> str:
        """
        決算日
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.DATE_OF_SETTLEMENT))

    @property
    def redeem_fee(self) -> str:
        """
        解約手数料
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.REDEEM_FEE))

    @property
    def subscribe_fee(self) -> str:
        """
        購入時手数料
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.SUBSCRIBE_FEE))

    @property
    def redemption_fee(self) -> str:
        """
        信託財産留保額
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.REDEMPTION_FEE))

    @property
    def management_fee(self) -> str:
        """
        運用管理報酬(信託報酬)
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.MANAGEMENT_FEE))

    @property
    def management_fee_for_investment_manager(self) -> str:
        """
        運用管理報酬(信託報酬)運用会社
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.MANAGEMENT_FEE_FOR_INVESTMENT_MANAGER))

    @property
    def management_fee_for_sales(self) -> str:
        """
        運用管理報酬(信託報酬)販売会社
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.MANAGEMENT_FEE_FOR_SALES))

    @property
    def management_fee_for_custody(self) -> str:
        """
        運用管理報酬(信託報酬)信託銀行
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.MANAGEMENT_FEE_FOR_CUSTODY))

    @property
    def historical_data_url(self) -> str:
        """
        基準価額・純資産総額・分配金のCSV データダウンロード
        :return:
        """

        return "https://toushin-lib.fwg.ne.jp" + self._sanitize(self._parse_element(*AttributeLocator.HISTORICAL_DATA_URL))

    @property
    def dividend(self) -> dict:
        """
        最大直近12ヶ月の分配金を取得する
        :return:
        """
        # dividends = []
        dividend_date = []
        dividend_amount = []

        for i in range(12):
            dividend_date_locator = AttributeLocator().get_distribution_date_locator(i)
            dividend_amount_locator = AttributeLocator().get_distribution_amount_locator(i)

            dividend_date.append(self._sanitize(self._parse_element(*dividend_date_locator)))
            dividend_amount.append(self._sanitize(self._parse_element(*dividend_amount_locator)))

        return {
            "date": dividend_date,
            "amount": dividend_amount
        }

    @property
    def dividend_total_of_year(self) -> str:
        """
        年間分配金累計
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.DIVIDEND_TOTAL_OF_YEAR))

    @property
    def fund_code(self) -> str:
        """
        協会ファンドコード
        :return:
        """
        return self._sanitize(self._parse_element(*AttributeLocator.FUND_CODE))

    @property
    def pct_change(self) -> dict:
        """
        騰落率を取得する
        :return:
        """
        period = []
        fund = []
        category = []

        for i in range(5):
            pct_change_period_locator = AttributeLocator().get_pct_change_period_locator(i)
            pct_change_fund_locator = AttributeLocator().get_pct_change_fund_locator(i)
            pct_change_category_locator = AttributeLocator().get_pct_change_category_locator(i)

            period.append(self._sanitize(self._parse_element(*pct_change_period_locator)))
            fund.append(self._sanitize(self._parse_element(*pct_change_fund_locator)))
            category.append(self._sanitize(self._parse_element(*pct_change_category_locator)))

        return {
            "period": period,
            "fund": fund,
            "category": category
        }

    @property
    def risk(self) -> dict:
        """
        騰落率を取得する
        :return:
        """
        period = []
        fund = []
        category = []

        for i in range(5):
            risk_period_locator = AttributeLocator().get_risk_period_locator(i)
            risk_fund_locator = AttributeLocator().get_risk_fund_locator(i)
            risk_category_locator = AttributeLocator().get_risk_category_locator(i)

            period.append(self._sanitize(self._parse_element(*risk_period_locator)))
            fund.append(self._sanitize(self._parse_element(*risk_fund_locator)))
            category.append(self._sanitize(self._parse_element(*risk_category_locator)))

        return {
            "period": period,
            "fund": fund,
            "category": category
        }

    @property
    def sharpe_ratio(self) -> dict:
        """
        騰落率を取得する
        :return:
        """
        period = []
        fund = []
        category = []

        for i in range(5):
            sharpe_ratio_period_locator = AttributeLocator().get_sharpe_ratio_period_locator(i)
            sharpe_ratio_fund_locator = AttributeLocator().get_sharpe_ratio_fund_locator(i)
            sharpe_ratio_category_locator = AttributeLocator().get_sharpe_ratio_category_locator(i)

            period.append(self._sanitize(self._parse_element(*sharpe_ratio_period_locator)))
            fund.append(self._sanitize(self._parse_element(*sharpe_ratio_fund_locator)))
            category.append(self._sanitize(self._parse_element(*sharpe_ratio_category_locator)))

        return {
            "period": period,
            "fund": fund,
            "category": category
        }
