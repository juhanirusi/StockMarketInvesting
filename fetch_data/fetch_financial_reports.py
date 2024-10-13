from datetime import date

import pandas as pd
import requests
from dateutil.relativedelta import relativedelta

from utils.get_api_keys import FMP_API_KEY

# Get last 20 years of data
CURRENT_DATE = date.today()
START_DATE = date.today() - relativedelta(years=20)


STOCK_TICKER = "ASML"


FMP_BASE_URL = "https://financialmodelingprep.com/api/v3/"
DATA_PERIOD = "annual"
FMP_URL_API_KEY_SUFFIX = f"apikey={FMP_API_KEY}"

FINANCIAL_STATEMENTS = ["income-statement", "balance-sheet-statement", "cash-flow-statement"]


# income_statement = pd.json_normalize(income_statement_response.json())
# balance_sheet_statement = pd.json_normalize(income_statement_response.json())
# cash_flow_statement = pd.json_normalize(income_statement_response.json())

FILE_NAME = f"{STOCK_TICKER}_income_statement.csv"
FILE_PATH = f"C:\Users\juhan\OneDrive\Omat Tiedostot\GitHub\StockMarketInvesting\data\{FILE_NAME}"

# income_statement.to_csv(FILE_PATH)


def fetch_financial_reports_to_csv_files(stock_ticker: str, financial_statement: str):

    try:
        financial_report_response = requests.get(f"{FMP_BASE_URL}{financial_statement}/{stock_ticker}?period={DATA_PERIOD}&{FMP_URL_API_KEY_SUFFIX}")
    except Exception:
        print("NOOOOOOOOOOOOOOOOO")

    financial_report_as_df = pd.json_normalize(financial_report_response.json())

    FILE_NAME = f"{stock_ticker}_{financial_statement}.csv"
    FILE_PATH = f"C:\Users\juhan\OneDrive\Omat Tiedostot\GitHub\StockMarketInvesting\data\{FILE_NAME}"


for financial_statement in FINANCIAL_STATEMENTS:

    fetch_financial_reports_to_csv_files(
        stock_ticker=STOCK_TICKER, financial_statement=financial_statement
    )