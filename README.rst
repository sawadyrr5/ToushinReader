About this library
##

Downloading japanese mutual fund data.
Data source `投信総合検索ライブラリー <https://toushin-lib.fwg.ne.jp/>`

How to install
##

::
    pip install git+https://github.com/sawadyrr5/ToushinReader

Usage
##
see example.py

::
    from ToushinReader.core import JPFund


    isin_code = "JP90C000KAH8"  # グローバルＥＳＧハイクオリティ成長株式ファンド（為替ヘッジなし）

    myFund = JPFund(isin_code)
    attrib = myFund.attribute
    print(attrib)

    result

::
    {'AS_OF_DATE': '2021年01月15日', 'FUND_NAME': 'グローバルＥＳＧハイクオリティ成長株式ファンド（為替ヘッジなし）', 'FUND_NICKNAME': '未来の世界（ＥＳＧ）', 'FUND_INVESTMENT_MANAGER': 'アセットマネジメントＯｎｅ', 'BASIC_PRICE': '11,366', 'NET_ASSET_AMOUNT': '888,785百万円', 'PRODUCT_CATEGORY': '追加型/ 内外/ 株式', 'INDEX_TYPE': '該当なし', 'ESTABLISH_DATE': '2020/07/20', 'CLOSING_DATE': '2030/07/12', 'DATE_TO_CLOSING': '9年6ヶ月', 'SETTLEMENT_FREQ': '年1回', 'DATE_OF_SETTLEMENT': '07/14', 'REDEEM_FEE': '外枠なし', 'SUBSCRIBE_FEE': '3.00%以内', 'REDEMPTION_FEE': '外枠0.5％未満', 'MANAGEMENT_FEE': '1.68000%', 'MANAGEMENT_FEE_FOR_INVESTMENT_MANAGER': '1.00000%', 'MANAGEMENT_FEE_FOR_SALES': '0.65000%', 'MANAGEMENT_FEE_FOR_CUSTODY': '0.03000%', 'LINK_HISTORICAL_DATA': 'https://toushin-lib.fwg.ne.jp/FdsWeb/FDST030000/csv-file-download?isinCd=JP90C000KAH8&associFundCd=47311207', 'BASIC_PRICE_YEN_CHANGE': '-183', 'BASIC_PRICE_PCT_CHANGE': '-1.58%'}
