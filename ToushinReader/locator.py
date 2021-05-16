# -*- coding: UTF-8 -*-
class AttributeLocator:
    # 評価基準日
    AS_OF_DATE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-3.d-flex.align-items-md-end.flex-md-column.mt-3.mt-md-0 > span",
        None,
    )
    # ファンド名
    FUND_NAME = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-9 > h3",
        None,
    )
    # 愛称
    FUND_NICKNAME = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-9 > div:nth-child(2)",
        None,
    )
    # 運用会社名
    FUND_INVESTMENT_MANAGER = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-9 > div:nth-child(3)",
        None,
    )
    # 基準価額
    BASIC_PRICE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(1) > div.d-flex > span",
        None,
    )
    # 基準価額前日比変化幅(上昇)
    BASIC_PRICE_YEN_POSITIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-positive-number-fg > div.d-flex > span",
        None,
    )
    # 基準価額前日比変化率(上昇)
    BASIC_PRICE_PCT_POSITIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-positive-number-fg > div.font-weight-normal > span",
        None,
    )
    # 基準価額前日比変化幅(下落)
    BASIC_PRICE_YEN_NEGATIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-negative-number-fg > div.d-flex > span",
        None,
    )
    # 基準価額前日比変化率(下落)
    BASIC_PRICE_PCT_NEGATIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-negative-number-fg > div.font-weight-normal > span",
        None,
    )
    # 純資産総額
    NET_ASSET_AMOUNT = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(3) > div:nth-child(2)",
        None,
    )
    # 商品分類
    PRODUCT_CATEGORY = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div.col-6.col-md-3.pl-md-5 > div.fds-font-size-0",
        None,
    )
    # インデックス型
    INDEX_TYPE = ("#tab_content1 > div > table > tr:nth-child(1) > td", None)
    # 設定尾
    ESTABLISH_DATE = (
        "#tab_content1 > div > table > tr:nth-child(2) > td",
        None,
    )
    # 償還日
    CLOSING_DATE = ("#tab_content1 > div > table > tr:nth-child(3) > td", None)
    # 償還までの期間
    DATE_TO_CLOSING = (
        "#tab_content1 > div > table > tr:nth-child(4) > td",
        None,
    )
    # 決算頻度
    SETTLEMENT_FREQ = (
        "#tab_content1 > div > table > tr:nth-child(5) > td",
        None,
    )
    # 決算日
    DATE_OF_SETTLEMENT = (
        "#tab_content1 > div > table > tr:nth-child(6) > td",
        None,
    )
    # 解約手数料
    REDEEM_FEE = (
        "#tab_content1 > div > table > tr:nth-child(8) > td",
        None,
    )
    # 購入時手数料
    SUBSCRIBE_FEE = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-7 > table > tbody > tr > td:nth-child(1)",
        None,
    )
    # 信託財産留保額
    REDEMPTION_FEE = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-7 > table > tbody > tr > td:nth-child(2)",
        None,
    )
    # 運用管理報酬(信託報酬)
    MANAGEMENT_FEE = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-7 > table > tbody > tr > td:nth-child(3)",
        None,
    )
    # 運用管理報酬(信託報酬)運用会社
    MANAGEMENT_FEE_FOR_INVESTMENT_MANAGER = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-4 > table > tr:nth-child(1) > td",
        None,
    )
    # 運用管理報酬(信託報酬)販売会社
    MANAGEMENT_FEE_FOR_SALES = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-4 > table > tr:nth-child(2) > td",
        None,
    )
    # 運用管理報酬(信託報酬)信託銀行
    MANAGEMENT_FEE_FOR_CUSTODY = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-4 > table > tr:nth-child(3) > td",
        None,
    )
    # 基準価額・純資産総額・分配金のCSVデータ
    LINK_HISTORICAL_DATA = ("#download", "href")

    # 分配金
    DISTRIBUTIONS = (
        "#dividendInfo",
        None
    )

    def get_distribution_date_locator(self, number: int):
        if isinstance(number, int):
            i = number + 2
            return f"#dividendInfo > tr:nth-child({i}) > th"

    def get_distribution_amount_locator(self, number: int):
        if isinstance(number, int):
            i = number + 2
            return f"#dividendInfo > tr:nth-child({i}) > td"

    def get_torakuritsu_period_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > table > tr:nth-child({i}) > th"

    def get_torakuritsu_fund_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > table > tr:nth-child({i}) > td:nth-child(2) > span"

    def get_torakuritsu_category_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > table > tr:nth-child({i}) > td:nth-child(3) > span"

    def get_risk_period_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > table > tr:nth-child({i}) > th"

    def get_risk_fund_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > table > tr:nth-child({i}) > td:nth-child(2) > span"

    def get_risk_category_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > table > tr:nth-child({i}) > td:nth-child(3) > span"

    def get_sr_period_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div > table > tr:nth-child({i}) > th"

    def get_sr_fund_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1)> div:nth-child(3) > div > table > tr:nth-child({i}) > td:nth-child(2) > span"

    def get_sr_category_locator(self, number: int) -> str:
        if isinstance(number, int):
            i = number + 3
            return f"#tab_content2 > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div > table > tr:nth-child({i}) > td:nth-child(3) > span"
