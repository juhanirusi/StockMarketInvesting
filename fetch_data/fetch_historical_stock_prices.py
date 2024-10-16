from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf
from dateutil.relativedelta import relativedelta

from utils.create_file_directories import HISTORICAL_STOCK_PRICES_DIR

# Get last 20 years of data
CURRENT_DATE = date.today()
START_DATE = date.today() - relativedelta(years=20)


def fetch_historical_data_to_csv_files(stock_ticker: str):

    try:
        historical_stock_price_data = pd.DataFrame(
            yf.download(
                tickers=stock_ticker,
                start=START_DATE,
                end=CURRENT_DATE,
                interval="1d",
                actions=True,
                # rounding=True,
            )
        )
        historical_stock_price_data.reset_index(inplace=True)
    except Exception:
        print("NOOOOOOOOOOOOOOOOO")

    FILE_PATH = f"{HISTORICAL_STOCK_PRICES_DIR}/{stock_ticker}"
    Path(FILE_PATH).mkdir(parents=True, exist_ok=True)

    historical_stock_price_data.to_csv(f"{FILE_PATH}/historical.csv", index=False)
