# -*- coding: utf-8 -*-
from ToushinReader.page import AttributePage


class JPFund:
    def __init__(self, isin_code: str):
        self.isin_code = isin_code
        self.attribute = AttributePage(isin_code).attributes()

    def distribution(self):
        d = AttributePage(self.isin_code).distribution()
        return d

    def torakuritsu(self):
        d = AttributePage(self.isin_code).torakuritsu()
        return d

    def risk(self):
        d = AttributePage(self.isin_code).risk()
        return d

    def sr(self):
        d = AttributePage(self.isin_code).sr()
        return d
