import pandas as pd
import requests
from src.config import ALPHA_VANTAGE_API_KEY

def extract_csv(csv_path):
    a = pd.read_csv(csv_path)
    return a

def av_extract(api):
    search_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "AAPL",
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    api_key=search_parameters[apikey]
    symbol=search_parameters[symbol]
    response_or_file = requests.get(api, params=search_parameters)
#.text is an attribute
    line_or_data = response_or_file.text
#.status_code is an attribute
    if response_or_file.status_code == 200:
        pass
    else:
        print(response_or_file.status_code)
    return line_or_data


