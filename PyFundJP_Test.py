#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
from PyFundJP import PyFundJP

# 日本株アルファ・カルテット（毎月分配型）
myFund = PyFundJP('JP90C000A931')

# 属性情報を取得する
print(myFund.attrib())

# 基準価格を取得する
print(myFund.nav('2015-01-01', '2015-06-30'))

# 所有期間損益, 分配金累計, 所有期間損益（分配金含む）, 収益率(年換算)を取得する
print(myFund.perf('2015-01-01', '2015-06-30', 1000000))
