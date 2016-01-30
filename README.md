# PyFundJP
日本国内の投資信託に関する情報取得ツール.

## 機能
###PyFundJP.detail()
属性情報を取得する

###PyFundJP.nav()
基準価格を取得する

## サンプル

```py:PyFundJP_Test.py
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
from PyFundJP import PyFundJP

myFund = PyFundJP('JP90C000A931')

# 属性情報を取得する
print(myFund.detail())

# 基準価格を取得する
print(myFund.nav(2015,1,1,2015,12,31))
```