import os
from datetime import date

import pandas as pd
import requests
import yfinance as yf
from dateutil.relativedelta import relativedelta

from utils.create_file_directories import CreateFileDirs
from utils.get_api_keys import FMP_API_KEY

create_file_directories = CreateFileDirs()


# Get last 20 years of data
CURRENT_DATE = date.today()
START_DATE = date.today() - relativedelta(years=20)


STOCK_TICKER = "ASML"


# FMP_BASE_URL = "https://financialmodelingprep.com/api/v3/"

# DATA_PERIOD = "annual"

# FMP_URL_API_KEY_SUFFIX = f"apikey={FMP_API_KEY}"

# INCOME_STATEMENT_DATA_URL = f"{FMP_BASE_URL}income-statement/{STOCK_TICKER}?period={DATA_PERIOD}&{FMP_URL_API_KEY_SUFFIX}"
# BALANCE_SHEET_STATEMENT_DATA_URL = f"{FMP_BASE_URL}balance-sheet-statement/{STOCK_TICKER}?period={DATA_PERIOD}&{FMP_URL_API_KEY_SUFFIX}"
# CASH_FLOW_STATEMENT_DATA_URL = f"{FMP_BASE_URL}cash-flow-statement/{STOCK_TICKER}?period={DATA_PERIOD}&{FMP_URL_API_KEY_SUFFIX}"

# income_statement_response = requests.get(INCOME_STATEMENT_DATA_URL)
# # balance_sheet_statement_response = requests.get(INCOME_STATEMENT_DATA_URL)
# # cash_flow_statement_response = requests.get(INCOME_STATEMENT_DATA_URL)

# data = pd.json_normalize(income_statement_response.json())
# print(data)

# FILE_NAME = f"{STOCK_TICKER}_income_statement.csv"
# FILE_PATH = rf"C:\Users\juhan\OneDrive\Omat Tiedostot\GitHub\StockMarketInvesting\data\{FILE_NAME}"

# data.to_csv(FILE_PATH)


company = pd.DataFrame(
    yf.download(
        tickers=STOCK_TICKER,
        start=START_DATE,
        end=CURRENT_DATE,
        interval="1d",
        actions=True,
        # rounding=True,
    )
)

company = company.reset_index()
company["Date"] = pd.to_datetime(company["Date"])

stock = yf.Ticker(STOCK_TICKER)
financial = stock.financials
print(financial)

actions = stock.get_actions()
balance = stock.get_balance_sheet()
calendar = stock.get_calendar()
cf = stock.get_cashflow()
info = stock.get_info()
inst_holders = stock.get_institutional_holders()
news = stock.get_news()
recommendations = stock.get_recommendations()

# PRINT THE RESULTS
print(actions)
print("*" * 20)
print(balance)
print("*" * 20)
print(calendar)
print("*" * 20)
print(cf)
print("*" * 20)
print(info)
print("*" * 20)
print(inst_holders)
print("*" * 20)
print(news)
print("*" * 20)
print(recommendations)
print("*" * 20)

print(company)

company.to_csv(
    r"C:\Users\juhan\OneDrive\Omat Tiedostot\GitHub\StockMarketInvesting\data\company.csv"
)

if __name__ == "__main__":
    if not FMP_API_KEY:
        print("REMEMBER TO ADD ENVIRONMENT VARIABLES !!!")

    create_file_directories.create_file_folders_if_not_exist()
