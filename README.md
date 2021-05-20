# About this library
Downloading japanese mutual fund data.
Data source [投信総合検索ライブラリー](https://toushin-lib.fwg.ne.jp/)

## How to install
```buildoutcfg
pip install ToushinReader
```

## Usage
see example.py
```buildoutcfg
from ToushinReader.core import Fund


isin_code = "JP90C000KAH8"  # グローバルＥＳＧハイクオリティ成長株式ファンド（為替ヘッジなし）

myFund = Fund(isin_code)
```
