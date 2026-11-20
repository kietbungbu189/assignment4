import pandas as pd
import functools
import numpy as np
import math

def aggregate_total(df):
    all_dates = []
    for column in df[:,2:]:
        a = {colum: df[:,column].value_counts()}
        all_dates.append(a)
    return all_dates
    