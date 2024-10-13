import os

from dotenv import load_dotenv

load_dotenv()

# API key to the https://financialmodelingprep.com/api
FMP_API_KEY = os.getenv("FMP_API_KEY")
