from datetime import date

import pandas as pd
import yfinance as yf
from dateutil.relativedelta import relativedelta

STOCK_TICKER = "ASML"
CURRENT_DATE = date.today()
START_DATE = date.today() - relativedelta(years=10)


company = pd.DataFrame(
    yf.download(
        tickers=STOCK_TICKER,
        start=START_DATE,
        end=CURRENT_DATE,
        interval="1d",
    )
)

print(company)
