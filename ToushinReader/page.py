# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from requests import Session
from ToushinReader.locator import AttributeLocator

from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

disable_warnings(InsecureRequestWarning)


class AttributePage:
    def __init__(self, isin_code: str):
        url = f"https://toushin-lib.fwg.ne.jp/FdsWeb/FDST030000?isinCd={isin_code}"

        self._create_soup(url)

    def _create_soup(self, url: str):
        self._soup = BeautifulSoup(
            Session().get(url, verify=False).text, features="html.parser"
        )

    def _parse_element(self, css_selector: str, attr: str = None) -> str:
        res = [
            elem.get(attr) if attr else elem.text
            for elem in self._soup.select(css_selector)
        ]

        if len(res) > 0:
            return res[0]

    def attributes(self) -> dict:
        res = {
            k: self._sanitize(self._parse_element(*v))
            for k, v in vars(AttributeLocator).items()
            if isinstance(v, tuple)
        }

        # 騰落表示
        if res["BASIC_PRICE_YEN_POSITIVE_CHANGE"]:
            res["BASIC_PRICE_YEN_CHANGE"] = res["BASIC_PRICE_YEN_POSITIVE_CHANGE"]
        elif res["BASIC_PRICE_YEN_NEGATIVE_CHANGE"]:
            res["BASIC_PRICE_YEN_CHANGE"] = "-" + res["BASIC_PRICE_YEN_NEGATIVE_CHANGE"]
        res.pop("BASIC_PRICE_YEN_POSITIVE_CHANGE")
        res.pop("BASIC_PRICE_YEN_NEGATIVE_CHANGE")

        if res["BASIC_PRICE_PCT_POSITIVE_CHANGE"]:
            res["BASIC_PRICE_PCT_CHANGE"] = (
                res["BASIC_PRICE_PCT_POSITIVE_CHANGE"].replace("(", "").replace(")", "")
            )
        elif res["BASIC_PRICE_PCT_NEGATIVE_CHANGE"]:
            res["BASIC_PRICE_PCT_CHANGE"] = "-" + res[
                "BASIC_PRICE_PCT_NEGATIVE_CHANGE"
            ].replace("(", "").replace(")", "")
        res.pop("BASIC_PRICE_PCT_POSITIVE_CHANGE")
        res.pop("BASIC_PRICE_PCT_NEGATIVE_CHANGE")

        # csvリンク
        if res["LINK_HISTORICAL_DATA"]:
            res["LINK_HISTORICAL_DATA"] = (
                    "https://toushin-lib.fwg.ne.jp" + res["LINK_HISTORICAL_DATA"]
            )

        return res

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

    def distribution(self) -> list:
        """
        最大直近12ヶ月の分配金を取得する
        :return:
        """
        distributions = []

        for i in range(12):
            distribution_date_locator = AttributeLocator().get_distribution_date_locator(i)
            distribution_amount_locator = AttributeLocator().get_distribution_amount_locator(i)

            distribution_date = self._parse_element(distribution_date_locator, None)
            distribution_amount = self._parse_element(distribution_amount_locator, None)

            # 決算日と分配金が取得できたら返り値に入れる
            if distribution_date and distribution_amount:
                distributions.append(
                    (
                        self._sanitize(distribution_date),
                        self._sanitize(distribution_amount)
                    )
                )

        return distributions

    def torakuritsu(self) -> list:
        """
        騰落率を取得する
        :return:
        """
        torakuritsu = []

        for i in range(12):
            torakuritsu_period_locator = AttributeLocator().get_torakuritsu_period_locator(i)
            torakuritsu_fund_locator = AttributeLocator().get_torakuritsu_fund_locator(i)
            torakuritsu_category_locator = AttributeLocator().get_torakuritsu_category_locator(i)

            torakuritsu_period = self._parse_element(torakuritsu_period_locator, None)
            torakuritsu_fund = self._parse_element(torakuritsu_fund_locator, None)
            torakuritsu_category = self._parse_element(torakuritsu_category_locator, None)

            # 決算日と分配金が取得できたら返り値に入れる
            if torakuritsu_period and torakuritsu_fund and torakuritsu_category:
                torakuritsu.append(
                    (
                        self._sanitize(torakuritsu_period),
                        self._sanitize(torakuritsu_fund),
                        self._sanitize(torakuritsu_category)
                    )
                )

        return torakuritsu

    def risk(self) -> list:
        """
        騰落率を取得する
        :return:
        """
        risk = []

        for i in range(12):
            risk_period_locator = AttributeLocator().get_risk_period_locator(i)
            risk_fund_locator = AttributeLocator().get_risk_fund_locator(i)
            risk_category_locator = AttributeLocator().get_risk_category_locator(i)

            risk_period = self._parse_element(risk_period_locator, None)
            risk_fund = self._parse_element(risk_fund_locator, None)
            risk_category = self._parse_element(risk_category_locator, None)

            # 決算日と分配金が取得できたら返り値に入れる
            if risk_period and risk_fund and risk_category:
                risk.append(
                    (
                        self._sanitize(risk_period),
                        self._sanitize(risk_fund),
                        self._sanitize(risk_category)
                    )
                )

        return risk

    def sr(self) -> list:
        """
        騰落率を取得する
        :return:
        """
        sr = []

        for i in range(12):
            sr_period_locator = AttributeLocator().get_sr_period_locator(i)
            sr_fund_locator = AttributeLocator().get_sr_fund_locator(i)
            sr_category_locator = AttributeLocator().get_sr_category_locator(i)

            sr_period = self._parse_element(sr_period_locator, None)
            sr_fund = self._parse_element(sr_fund_locator, None)
            sr_category = self._parse_element(sr_category_locator, None)

            # 決算日と分配金が取得できたら返り値に入れる
            if sr_period and sr_fund and sr_category:
                sr.append(
                    (
                        self._sanitize(sr_period),
                        self._sanitize(sr_fund),
                        self._sanitize(sr_category)
                    )
                )

        return sr
