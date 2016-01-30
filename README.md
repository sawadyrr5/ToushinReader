# PyFundJP
日本国内の投資信託に関する情報取得スクリプト.

## 動作環境
Python 3.5

lxml 3.5.0

pandas 0.17.1

## 機能
情報の取得元は[投信総合検索ライブラリー](http://tskl.toushin.or.jp/)です.
投資信託の銘柄はISINコードで指定します.

### PyFundJP.attrib()
属性情報を取得する.

### PyFundJP.nav(date_from, date_to)
基準価格を取得する.
返り値はpandas.DataFrame形式です.

### PyFundJP.perf(date_from, date_to, amount_money)
分配金込損益率を取得する.