from datetime import date
from pathlib import Path

import pandas as pd
import requests
import yfinance as yf
from dateutil.relativedelta import relativedelta

from utils.create_file_directories import (
    FINANCIAL_REPORTS_DIR,
    HISTORICAL_STOCK_PRICES_DIR,
    STOCK_ANALYST_RECOMMENDATIONS_DIR,
    STOCK_ESTIMATES_DIR,
    STOCK_INSTITUTIONAL_HOLDERS_DIR,
    STOCK_RATIOS_AND_MARGINS_DIR,
    STOCK_SPLITS_AND_DIVIDENDS_DIR,
)
from utils.get_api_keys import FMP_API_KEY

# Get last 20 years of data
CURRENT_DATE = date.today()
START_DATE = date.today() - relativedelta(years=20)


class FetchDataForStock:

    def __init__(self):

        self.FMP_BASE_URL = "https://financialmodelingprep.com/api/v3/"
        self.DATA_PERIOD = "annual"
        self.FMP_URL_API_KEY_SUFFIX = f"apikey={FMP_API_KEY}"

        self.FINANCIAL_STATEMENTS_TO_FETCH = [
            "income-statement",
            "balance-sheet-statement",
            "cash-flow-statement",
        ]

    def fetch_financial_reports_to_csv_files(
        self, stock_ticker: str, financial_statement: str
    ):

        try:
            financial_report_response = requests.get(
                f"{self.FMP_BASE_URL}{financial_statement}/{stock_ticker}?period={self.DATA_PERIOD}&{self.FMP_URL_API_KEY_SUFFIX}"
            )
        except Exception as exception:
            print(
                f"Fetching {stock_ticker}'s financial statement - '{financial_statement}' data ended up in a exception - {exception}"
            )

        financial_report_as_df = pd.json_normalize(financial_report_response.json())

        FILE_PATH = f"{FINANCIAL_REPORTS_DIR}/{stock_ticker}"
        Path(FILE_PATH).mkdir(exist_ok=True)

        financial_report_as_df.to_csv(
            f"{FILE_PATH}/{financial_statement}.csv", index=False
        )

    def _fetch_stock_and_company_data(self, stock_ticker: str):
        self.fetch_historical_data_to_csv_file(stock_ticker)
        self.fetch_dividend_and_stock_split_data_to_csv_file(stock_ticker)
        self.fetch_future_estimates_data_to_csv_file(stock_ticker)
        self.fetch_institutional_holders_data_to_csv_file(stock_ticker)
        self.fetch_stock_ratios_and_margins_data_to_csv_file(stock_ticker)
        self.fetch_analyst_recommendations_data_to_csv_file(stock_ticker)

    def fetch_historical_data_to_csv_file(self, stock_ticker: str):

        try:
            historical_stock_price_data = pd.DataFrame(
                yf.download(
                    tickers=stock_ticker,
                    start=START_DATE,
                    end=CURRENT_DATE,
                    interval="1d",  # Daily based stock data
                    # actions=True,
                    # rounding=True,
                )
            )
            historical_stock_price_data.reset_index(inplace=True)
        except Exception as exception:
            print(
                f"Fetching {stock_ticker}'s historical data ended up in a exception - {exception}"
            )

        FILE_PATH = f"{HISTORICAL_STOCK_PRICES_DIR}/{stock_ticker}"
        Path(FILE_PATH).mkdir(parents=True, exist_ok=True)

        historical_stock_price_data.to_csv(f"{FILE_PATH}/historical.csv", index=False)

    def fetch_dividend_and_stock_split_data_to_csv_file(self, stock_ticker: str):

        try:
            stock_dividend_and_stock_split_data = pd.DataFrame(
                yf.Ticker(stock_ticker).get_actions()
            )
            stock_dividend_and_stock_split_data.reset_index(inplace=True)
        except Exception as exception:
            print(
                f"Fetching {stock_ticker}'s dividend and stock split data ended up in a exception - {exception}"
            )

        FILE_PATH = f"{STOCK_SPLITS_AND_DIVIDENDS_DIR}/{stock_ticker}"
        Path(FILE_PATH).mkdir(parents=True, exist_ok=True)

        stock_dividend_and_stock_split_data.to_csv(
            f"{FILE_PATH}/stock-split-and-dividends.csv", index=False
        )

    def fetch_future_estimates_data_to_csv_file(self, stock_ticker: str):

        try:
            stock_future_estimates_data = pd.DataFrame(
                yf.Ticker(stock_ticker).get_calendar()
            )
        except Exception as exception:
            print(
                f"Fetching {stock_ticker}'s future estimates data ended up in a exception - {exception}"
            )

        FILE_PATH = f"{STOCK_ESTIMATES_DIR}/{stock_ticker}"
        Path(FILE_PATH).mkdir(parents=True, exist_ok=True)

        stock_future_estimates_data.to_csv(
            f"{FILE_PATH}/stock-future-estimates.csv", index=False
        )

    def fetch_institutional_holders_data_to_csv_file(self, stock_ticker: str):

        try:
            stock_future_estimates_data = pd.DataFrame(
                yf.Ticker(stock_ticker).get_institutional_holders()
            )
        except Exception as exception:
            print(
                f"Fetching {stock_ticker}'s institutional holders data ended up in a exception - {exception}"
            )

        FILE_PATH = f"{STOCK_INSTITUTIONAL_HOLDERS_DIR}/{stock_ticker}"
        Path(FILE_PATH).mkdir(parents=True, exist_ok=True)

        stock_future_estimates_data.to_csv(
            f"{FILE_PATH}/stock-institutional-holders.csv", index=False
        )

    def fetch_stock_ratios_and_margins_data_to_csv_file(self, stock_ticker: str):

        try:
            stock_ratios_and_margins_data = pd.DataFrame(
                yf.Ticker(stock_ticker).get_info()
            )
        except Exception as exception:
            print(
                f"Fetching {stock_ticker}'s ratios and margins data ended up in a exception - {exception}"
            )

        FILE_PATH = f"{STOCK_RATIOS_AND_MARGINS_DIR}/{stock_ticker}"
        Path(FILE_PATH).mkdir(parents=True, exist_ok=True)

        stock_ratios_and_margins_data.to_csv(
            f"{FILE_PATH}/stock-ratios-and-margins.csv", index=False
        )

    def fetch_analyst_recommendations_data_to_csv_file(self, stock_ticker: str):

        try:
            stock_ratios_and_margins_data = pd.DataFrame(
                yf.Ticker(stock_ticker).get_recommendations()
            )
        except Exception as exception:
            print(
                f"Fetching {stock_ticker}'s analyst recommendations data ended up in a exception - {exception}"
            )

        FILE_PATH = f"{STOCK_ANALYST_RECOMMENDATIONS_DIR}/{stock_ticker}"
        Path(FILE_PATH).mkdir(parents=True, exist_ok=True)

        stock_ratios_and_margins_data.to_csv(
            f"{FILE_PATH}/stock-analyst-recommendations.csv", index=False
        )
