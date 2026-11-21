import pandas as pd
import numpy as np
from datetime import datetime

def convert_date(date):
#use strptime (date type -> text) instead of strftime (text...
#... -> date type)
    x = datetime.strptime(date, "%m/%d/%y")
    return x

def flatten_data(json_data):
    selected_columns = ['day', 'open', 'high', 'low', 'close', 'volume']
    df_json = pd.DataFrame(columns=selected_columns)
#This uses the same idea as COVID-19 dictionaries
    for key, column in df_json.items(): 
        df_json["day"] = json_data["Time Series (Daily)"].keys()[1] 
        df_json["open"] = json_data["Time Series (Daily)"][key]["open"]


