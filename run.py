import pandas as pd
import yfinance as yf

from fetch_data.fetch_stock_data import FetchDataForStock
from utils.create_file_directories import CreateFileDirs
from utils.get_api_keys import FMP_API_KEY

create_file_directories = CreateFileDirs()
fetch_stock_data = FetchDataForStock()


STOCK_TICKER = "ASML"


# stock = yf.Ticker(STOCK_TICKER)
# print(stock)

# calendar = stock.get_calendar()  # --> Dividend dates, earnings date, EPS and Revenue estimates
# info = stock.get_info()  # --> Useful info and different ratios
# inst_holders = stock.get_institutional_holders() # --> See institutional holders/percentages/value
# recommendations = stock.get_recommendations() # --> Get recommendations from analysts

# # PRINT THE RESULTS
# print(actions)
# print(calendar)
# print(info)
# print(inst_holders)
# print(recommendations)

# print(company)

# company.to_csv(
#     r"C:\Users\juhan\OneDrive\Omat Tiedostot\GitHub\StockMarketInvesting\data\company.csv"
# )

if __name__ == "__main__":

    if not FMP_API_KEY:
        print("REMEMBER TO ADD ENVIRONMENT VARIABLES !!!")

    create_file_directories.create_file_folders_if_not_exist()

    for financial_statement in fetch_stock_data.FINANCIAL_STATEMENTS_TO_FETCH:

        fetch_stock_data.fetch_financial_reports_to_csv_files(
            stock_ticker=STOCK_TICKER, financial_statement=financial_statement
        )

    fetch_stock_data.fetch_historical_data_to_csv_file(stock_ticker=STOCK_TICKER)
    fetch_stock_data.fetch_dividend_and_stock_split_data_to_csv_file(
        stock_ticker=STOCK_TICKER
    )
