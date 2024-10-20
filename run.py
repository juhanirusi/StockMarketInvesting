from fetch_data.fetch_stock_data import FetchDataForStock
from utils.create_file_directories import CreateFileDirs
from utils.get_api_keys import FMP_API_KEY

create_file_dirs = CreateFileDirs()
fetch_stock_data = FetchDataForStock()

STOCK_TICKER = "ASML"


if __name__ == "__main__":

    if not FMP_API_KEY:
        print("REMEMBER TO ADD ENVIRONMENT VARIABLES !!!")

    RAW_DATA_DIR = create_file_dirs.create_stock_raw_data_folder(STOCK_TICKER)
    MANIPULATED_DATA_DIR = create_file_dirs.create_stock_manipulated_data_folder(
        STOCK_TICKER
    )

    # --------------- Fetch Data ---------------

    fetch_stock_data._fetch_stocks_financial_reports_and_company_data(
        raw_data_dir=RAW_DATA_DIR, stock_ticker=STOCK_TICKER
    )

    # --------------- Manipulate Data ---------------
