import os
from datetime import date

import pandas as pd
import requests
import yfinance as yf
from dateutil.relativedelta import relativedelta

from fetch_data.fetch_financial_reports import (
    FINANCIAL_STATEMENTS,
    fetch_financial_reports_to_csv_files,
)
from fetch_data.fetch_historical_stock_prices import fetch_historical_data_to_csv_files
from utils.create_file_directories import CreateFileDirs
from utils.get_api_keys import FMP_API_KEY

create_file_directories = CreateFileDirs()


# Get last 20 years of data
CURRENT_DATE = date.today()
START_DATE = date.today() - relativedelta(years=20)


STOCK_TICKER = "ASML"


# stock = yf.Ticker(STOCK_TICKER)
# financial = stock.financials
# print(financial)

# actions = stock.get_actions()
# balance = stock.get_balance_sheet()
# calendar = stock.get_calendar()
# cf = stock.get_cashflow()
# info = stock.get_info()
# inst_holders = stock.get_institutional_holders()
# news = stock.get_news()
# recommendations = stock.get_recommendations()

# # PRINT THE RESULTS
# print(actions)
# print("*" * 20)
# print(balance)
# print("*" * 20)
# print(calendar)
# print("*" * 20)
# print(cf)
# print("*" * 20)
# print(info)
# print("*" * 20)
# print(inst_holders)
# print("*" * 20)
# print(news)
# print("*" * 20)
# print(recommendations)
# print("*" * 20)

# print(company)

# company.to_csv(
#     r"C:\Users\juhan\OneDrive\Omat Tiedostot\GitHub\StockMarketInvesting\data\company.csv"
# )

if __name__ == "__main__":

    if not FMP_API_KEY:
        print("REMEMBER TO ADD ENVIRONMENT VARIABLES !!!")

    create_file_directories.create_file_folders_if_not_exist()

    for financial_statement in FINANCIAL_STATEMENTS:

        fetch_financial_reports_to_csv_files(
            stock_ticker=STOCK_TICKER, financial_statement=financial_statement
        )

        fetch_historical_data_to_csv_files(stock_ticker=STOCK_TICKER)
