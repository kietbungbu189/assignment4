import pandas as pd
import requests

def extract_csv(csv_path):
    a = pd.read_csv(csv_path)
    return a

def av_extract(api):
    line_or_data = requests.get(api)
    text = line_or_data.text()


