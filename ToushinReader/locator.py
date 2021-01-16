# -*- coding: UTF-8 -*-
class AttributeLocator:
    AS_OF_DATE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-3.d-flex.align-items-md-end.flex-md-column.mt-3.mt-md-0 > span",
        None,
    )
    FUND_NAME = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-9 > h3",
        None,
    )
    FUND_NICKNAME = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-9 > div:nth-child(2)",
        None,
    )
    FUND_INVESTMENT_MANAGER = (
        "body > div.fds-image-top-message.mb-4 > div > div > div:nth-child(1) > div.col-md-9 > div:nth-child(3)",
        None,
    )
    BASIC_PRICE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(1) > div.d-flex > span",
        None,
    )
    BASIC_PRICE_YEN_POSITIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-positive-number-fg > div.d-flex > span",
        None,
    )
    BASIC_PRICE_PCT_POSITIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-positive-number-fg > div.font-weight-normal > span",
        None,
    )
    BASIC_PRICE_YEN_NEGATIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-negative-number-fg > div.d-flex > span",
        None,
    )
    BASIC_PRICE_PCT_NEGATIVE_CHANGE = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(2) > div.fds-negative-number-fg > div.font-weight-normal > span",
        None,
    )
    NET_ASSET_AMOUNT = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div:nth-child(3) > div:nth-child(2)",
        None,
    )
    PRODUCT_CATEGORY = (
        "body > div.fds-image-top-message.mb-4 > div > div > div.row.no-gutters.font-weight-bold > div.col-6.col-md-3.pl-md-5 > div.fds-font-size-0",
        None,
    )

    INDEX_TYPE = ("#tab_content1 > div > table > tr:nth-child(1) > td", None)
    ESTABLISH_DATE = (
        "#tab_content1 > div > table > tr:nth-child(2) > td",
        None,
    )
    CLOSING_DATE = ("#tab_content1 > div > table > tr:nth-child(3) > td", None)
    DATE_TO_CLOSING = (
        "#tab_content1 > div > table > tr:nth-child(4) > td",
        None,
    )
    SETTLEMENT_FREQ = (
        "#tab_content1 > div > table > tr:nth-child(5) > td",
        None,
    )
    DATE_OF_SETTLEMENT = (
        "#tab_content1 > div > table > tr:nth-child(6) > td",
        None,
    )
    REDEEM_FEE = (
        "#tab_content1 > div > table > tr:nth-child(8) > td",
        None,
    )
    SUBSCRIBE_FEE = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-7 > table > tbody > tr > td:nth-child(1)",
        None,
    )
    REDEMPTION_FEE = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-7 > table > tbody > tr > td:nth-child(2)",
        None,
    )
    MANAGEMENT_FEE = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-7 > table > tbody > tr > td:nth-child(3)",
        None,
    )
    MANAGEMENT_FEE_FOR_INVESTMENT_MANAGER = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-4 > table > tr:nth-child(1) > td",
        None,
    )
    MANAGEMENT_FEE_FOR_SALES = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-4 > table > tr:nth-child(2) > td",
        None,
    )
    MANAGEMENT_FEE_FOR_CUSTODY = (
        "#tab_content1 > div > div:nth-child(2) > div > div.col-md-4 > table > tr:nth-child(3) > td",
        None,
    )
    LINK_HISTORICAL_DATA = ("#download", "href")
