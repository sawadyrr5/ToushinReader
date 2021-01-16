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
