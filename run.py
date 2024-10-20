import pandas as pd
import yfinance as yf

from fetch_data.fetch_stock_data import FetchDataForStock
from utils.create_file_directories import CreateFileDirs
from utils.get_api_keys import FMP_API_KEY

create_file_directories = CreateFileDirs()
fetch_stock_data = FetchDataForStock()


STOCK_TICKER = "ASML"


if __name__ == "__main__":

    if not FMP_API_KEY:
        print("REMEMBER TO ADD ENVIRONMENT VARIABLES !!!")

    create_file_directories.create_file_folders_if_not_exist()

    for financial_statement in fetch_stock_data.FINANCIAL_STATEMENTS_TO_FETCH:

        fetch_stock_data.fetch_financial_reports_to_csv_files(
            stock_ticker=STOCK_TICKER, financial_statement=financial_statement
        )

    fetch_stock_data._fetch_stock_and_company_data(stock_ticker=STOCK_TICKER)
