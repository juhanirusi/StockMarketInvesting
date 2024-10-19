import os

CWD = os.getcwd()  # Get the current working directory

DATA_DIR = f"{CWD}/data"
FINANCIAL_REPORTS_DIR = f"{DATA_DIR}/financial-reports"
HISTORICAL_STOCK_PRICES_DIR = f"{DATA_DIR}/historical-stock-prices"
STOCK_SPLITS_AND_DIVIDENDS_DIR = f"{DATA_DIR}/stock-splits-and-dividends"

DIRECTORIES = [
    DATA_DIR,
    FINANCIAL_REPORTS_DIR,
    HISTORICAL_STOCK_PRICES_DIR,
    STOCK_SPLITS_AND_DIVIDENDS_DIR,
]


class CreateFileDirs:

    def create_file_folders_if_not_exist(self):

        for directory in DIRECTORIES:

            if not os.path.exists(directory):
                os.makedirs(directory)
