import os

CWD = os.getcwd()  # Get the current working directory

DATA_DIR = f"{CWD}/data"
FINANCIAL_REPORTS_DIR = f"{DATA_DIR}/financial-reports"
HISTORICAL_STOCK_PRICES_DIR = f"{DATA_DIR}/historical-stock-prices"
STOCK_SPLITS_AND_DIVIDENDS_DIR = f"{DATA_DIR}/stock-splits-and-dividends"
STOCK_ESTIMATES_DIR = f"{DATA_DIR}/stock-estimates"
STOCK_INSTITUTIONAL_HOLDERS_DIR = f"{DATA_DIR}/stock-institutional-holders"
STOCK_RATIOS_AND_MARGINS_DIR = f"{DATA_DIR}/stock-ratios-and-margins"
STOCK_ANALYST_RECOMMENDATIONS_DIR = f"{DATA_DIR}/stock-analyst-recommendations"

DIRECTORIES = [
    DATA_DIR,
    FINANCIAL_REPORTS_DIR,
    HISTORICAL_STOCK_PRICES_DIR,
    STOCK_SPLITS_AND_DIVIDENDS_DIR,
    STOCK_ESTIMATES_DIR,
    STOCK_INSTITUTIONAL_HOLDERS_DIR,
    STOCK_RATIOS_AND_MARGINS_DIR,
    STOCK_ANALYST_RECOMMENDATIONS_DIR,
]


class CreateFileDirs:

    def create_file_folders_if_not_exist(self):

        for directory in DIRECTORIES:

            if not os.path.exists(directory):
                os.makedirs(directory)
