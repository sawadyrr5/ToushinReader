#!/usr/local/bin python
# -*- coding: UTF-8 -*-
from pandas_datareader.base import _BaseReader
from pandas_datareader import data
import urllib.request
import urllib.error
import lxml.html
import pandas as pd

from JPFundDataReader.io.locator import AttributeLocator, AttributeFundLocator, AttributeMRFLocator, NAVLocator, \
    ReturnLocator

from datetime import datetime, timedelta

_SLEEP_TIME = 0.5
_MAX_RETRY_COUNT = 3


class JPFundReader(_BaseReader):
    locator = None

    @property
    def url(self):
        return self.locator.url


class AttributeReader(JPFundReader):
    locator = AttributeLocator()

    def read(self):
        # Use _DailyBaseReader's definition
        df = self._read_one_data(self.url, params=self._get_params(self.symbols))
        return df

    def _get_params(self, symbol):
        params = {
            'isinCd': symbol
        }
        return params

    def _read_one_data(self, url, params):
        url = self.url.format(**params)

        html = urllib.request.urlopen(url).read()
        root = lxml.html.fromstring(html)

        if '日々決算型' in root.xpath(self.locator.xpath['大分類'])[0].text:
            self.locator = AttributeMRFLocator()
        else:
            self.locator = AttributeFundLocator()

        result = {}
        for k, v in self.locator.xpath.items():
            res = root.xpath(v)

            if isinstance(res, list) and len(res) > 0:
                result[k] = res[0].text
            elif isinstance(res, str):
                result[k] = res.text
            else:
                result[k] = None

            if isinstance(result[k], str):
                result[k] = result[k].replace('\n', '')

        return result


class NAVReader(JPFundReader):
    locator = NAVLocator()

    def __init__(self, symbols=None, start=None, end=None, **kwargs):
        super(NAVReader, self).__init__(symbols=symbols,
                                        start=start,
                                        end=end,
                                        **kwargs)
        self.date_from = self.start
        self.date_to = self.end

    def read(self):
        # Use _DailyBaseReader's definition
        attribute = DataReader(self.symbols, data_source='attribute')
        self.date_from = max([self.start, datetime.strptime(attribute['設定日'], '%Y/%m/%d')])

        dfs = []
        while True:
            self.date_to = min([self.end, self.date_from + timedelta(days=90)])

            dfs.append(self._read_one_data(self.url, params=self._get_params(self.symbols)))

            self.date_from = self.date_to + timedelta(days=1)
            if self.date_from > self.end:
                break

        result = pd.concat(dfs)
        return result

    def _get_params(self, symbol):
        params = {
            'isinCd': symbol,
            'sy': self.date_from.year,
            'sm': str(self.date_from.month).zfill(2),
            'sd': str(self.date_from.day).zfill(2),
            'ey': self.date_to.year,
            'em': str(self.date_to.month).zfill(2),
            'ed': str(self.date_to.day).zfill(2)
        }
        return params

    def _read_one_data(self, url, params):
        url = self.url.format(**params)
        response = urllib.request.urlopen(url)
        try:
            df = pd.read_csv(response, encoding='Shift_JIS')
        except ValueError:
            df = pd.DataFrame()

        df['年月日'] = df['年月日'].apply(lambda s: pd.to_datetime(s, format=u'%Y年%m月%d日'))

        return df


class ReturnReader(JPFundReader):
    locator = ReturnLocator()

    def __init__(self, symbols=None, start=None, end=None, buy_amount_money=10000, **kwargs):
        super(ReturnReader, self).__init__(symbols=symbols,
                                           start=start,
                                           end=end,
                                           **kwargs)
        self.buy_amount_money = buy_amount_money
        self.date_from = self.start
        self.date_to = self.end

    def read(self):
        # Use _DailyBaseReader's definition
        result = self._read_one_data(self.url, params=self._get_params(self.symbols))
        return result

    def _get_params(self, symbol):
        params = {
            'isinCd': symbol,
            'sy': self.date_from.year,
            'sm': str(self.date_from.month).zfill(2),
            'sd': str(self.date_from.day).zfill(2),
            'ey': self.date_to.year,
            'em': str(self.date_to.month).zfill(2),
            'ed': str(self.date_to.day).zfill(2),
            'buyAmntMoney': self.buy_amount_money
        }
        return params

    def _read_one_data(self, url, params):
        url = self.url.format(**params)

        html = urllib.request.urlopen(url).read()
        root = lxml.html.fromstring(html)

        result = {}
        for k_ctg, v_ctg in self.locator.xpath.items():
            result[k_ctg] = {}
            for k, v in v_ctg.items():
                res = root.xpath(v)

                if isinstance(res, list) and len(v) > 0:
                    result[k_ctg][k] = res[0].text
                elif isinstance(v, str):
                    result[k_ctg][k] = res.text
                else:
                    result[k_ctg][k] = None

                if isinstance(result[k_ctg][k], str):
                    result[k_ctg][k] = result[k_ctg][k].replace('\n', '')

        return result


class SymbolError(Exception):
    pass


def DataReader(symbols, data_source=None, start=None, end=None, **kwargs):
    if data_source == 'attribute':
        return AttributeReader(symbols=symbols, **kwargs).read()
    elif data_source == 'nav':
        return NAVReader(symbols=symbols, start=start, end=end, **kwargs).read()
    elif data_source == 'return':
        buy_amount_money = kwargs.pop('buy_amount_money', None)
        return ReturnReader(symbols=symbols, start=start, end=end, buy_amount_money=buy_amount_money, **kwargs).read()
    else:
        return data.DataReader(name=symbols, data_source=data_source, start=start, end=end, **kwargs)


DataReader.__doc__ = data.DataReader.__doc__

if __name__ == '__main__':
    attribute = DataReader('JP90C0002V65', data_source='attribute')
    print(
        attribute
    )

    attribute = DataReader('JP90C000A931', data_source='attribute')
    print(
        attribute
    )

    attribute = DataReader('JP90C000EGU1', data_source='attribute')
    print(
        attribute
    )

    start = datetime(2017, 1, 1)
    end = datetime(2017, 1, 31)

    nav = DataReader('JP90C000A931', data_source='nav', start=start, end=end)
    print(
        nav
    )

    ret = DataReader('JP90C000A931', data_source='return', start=start, end=end, buy_amount_money=1000000)
    print(
        ret
    )
