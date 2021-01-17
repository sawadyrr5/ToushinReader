# -*- coding: utf-8 -*-
from ToushinReader.core import JPFund


isin_code = "JP90C000KAH8"  # グローバルＥＳＧハイクオリティ成長株式ファンド（為替ヘッジなし）

myFund = JPFund(isin_code)
attrib = myFund.attribute
print(attrib)
