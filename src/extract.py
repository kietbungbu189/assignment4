import pandas as pd
import requests

def extract_csv(csv_path):
    a = pd.read_csv(csv_path)
    return a

def av_extract(api):
    search_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "AAPL",
        "apikey": "AQBXLQR83N391L55"
    }
    response_or_file = requests.get(api, params=search_parameters)
    line_or_data = response_or_file.text()
    if response_or_file.status_code() == 200:
        pass
    else:
        print(response_or_file.status_code())
    return line_or_data


