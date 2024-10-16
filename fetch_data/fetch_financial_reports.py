from datetime import date
from pathlib import Path

import pandas as pd
import requests
from dateutil.relativedelta import relativedelta

from utils.create_file_directories import FINANCIAL_REPORTS_DIR
from utils.get_api_keys import FMP_API_KEY

# Get last 20 years of data
CURRENT_DATE = date.today()
START_DATE = date.today() - relativedelta(years=20)


FMP_BASE_URL = "https://financialmodelingprep.com/api/v3/"
DATA_PERIOD = "annual"
FMP_URL_API_KEY_SUFFIX = f"apikey={FMP_API_KEY}"

FINANCIAL_STATEMENTS = [
    "income-statement",
    "balance-sheet-statement",
    "cash-flow-statement",
]


def fetch_financial_reports_to_csv_files(stock_ticker: str, financial_statement: str):

    try:
        financial_report_response = requests.get(
            f"{FMP_BASE_URL}{financial_statement}/{stock_ticker}?period={DATA_PERIOD}&{FMP_URL_API_KEY_SUFFIX}"
        )
    except Exception:
        print("NOOOOOOOOOOOOOOOOO")

    financial_report_as_df = pd.json_normalize(financial_report_response.json())

    FILE_PATH = f"{FINANCIAL_REPORTS_DIR}/{stock_ticker}"
    Path(FILE_PATH).mkdir(exist_ok=True)

    print(FILE_PATH)

    financial_report_as_df.to_csv(f"{FILE_PATH}/{financial_statement}.csv", index=False)
