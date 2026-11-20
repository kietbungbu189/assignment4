import pandas as pd
import functools
import numpy as np
import math

def aggregate_total(df):
    all_dates = []
    for column in df[:,4:]:
        all_dates[column] = df.iloc[:,column].sum()
    return all_dates
    