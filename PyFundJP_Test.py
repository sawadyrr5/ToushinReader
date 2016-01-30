#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
from PyFundJP import PyFundJP

myFund = PyFundJP('JP90C000A931')

# 属性情報を取得する
print(myFund.detail())

# 基準価格を取得する
print(myFund.nav(2015,1,1,2015,12,31))