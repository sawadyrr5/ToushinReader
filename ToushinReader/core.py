# -*- coding: utf-8 -*-
from ToushinReader.page import AttributePage


class JPFund:
    def __init__(self, isin_code: str):
        self.isin_code = isin_code
        self.attribute = AttributePage(isin_code).attributes()
