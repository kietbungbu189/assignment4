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
    dict_list = []
    for key, column in metrics.items(): 
#.keys() returns a dict_keys view object, which does not...
#... support indexing
#        close_price = metrics["4. close"]
        dict = {}        
        dict['day'] = key
        dict['open'] = column["1. open"]
        dict['high'] = column["2. high"]
        dict['low'] = column["3. low"]
        dict['close'] = column["4. close"]
        dict['volume'] = column["5. volume"]
        dict_list.append(dict)
#        columns = {}
#
#        for column, index in zip(columns_names, target_column_position):
#            columns[column] = df_data.iloc[:, index]
#
#        df_data3 = pd.DataFrame(columns)
    df_json1 = pd.DataFrame(dict_list)

