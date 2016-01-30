#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
from PyFundJP import PyFundJP

myFund = PyFundJP('JP90C000A931')

print(myFund.detail())

#print(myFund.nav(2015,1,1,2015,3,31))

print(myFund.nav(2015,1,1,2015,12,31))