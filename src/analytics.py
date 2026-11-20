import pandas as pd
import functools
import numpy as np
import math

def aggregate_total(df):
    all_dates = []
    for column in df[:,4:]:
        a[column] = {colum: df[:,column].sum()}
        all_dates.append(a)
    return all_dates
    