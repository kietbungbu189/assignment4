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
    metrics = json_data["Time Series (Daily)"]
#This uses the same idea as COVID-19 dictionaries
    for key, column in metrics.items(): 
#.keys() returns a dict_keys view object, which does not...
#... support indexing
#        close_price = metrics["4. close"]        
        df_json['day'] = metrics2 = metrics[key]         
        df_json['open'] = metrics2["1. open"]
        df_json['high'] = metrics2["1. high"]
        df_json['low'] = metrics2["1. low"]
        df_json['close'] = metrics2["1. close"]
        df_json['volume'] = metrics2["1. volume"]


