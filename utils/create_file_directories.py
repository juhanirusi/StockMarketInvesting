import os
from pathlib import Path

CWD = os.getcwd()  # Get the current working directory


DATA_DIR = f"{CWD}/data"

RAW_DATA_DIR = f"{DATA_DIR}/raw_data"
MANIPULATED_DATA_DIR = f"{DATA_DIR}/manipulated_data"

STOCK_RAW_DATA_DIR = "None"
STOCK_MANIPULATED_DATA_DIR = "None"


class CreateFileDirs:

    def create_stock_raw_data_folder(self, stock_ticker: str) -> str:

        STOCK_RAW_DATA_DIR = f"{RAW_DATA_DIR}/{stock_ticker}"

        Path(STOCK_RAW_DATA_DIR).mkdir(parents=True, exist_ok=True)

        return STOCK_RAW_DATA_DIR

    def create_stock_manipulated_data_folder(self, stock_ticker: str) -> str:

        STOCK_MANIPULATED_DATA_DIR = f"{MANIPULATED_DATA_DIR}/{stock_ticker}"

        Path(STOCK_MANIPULATED_DATA_DIR).mkdir(parents=True, exist_ok=True)

        return STOCK_MANIPULATED_DATA_DIR
