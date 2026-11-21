import pandas as pd
import functools
import numpy as np
import math
import matplotlib.pyplot as plt

def aggregate_total(df):
#if...
#    all_dates = []    
#... then use enumerate() in main()
    all_dates = {}
#this works too:
#    for column in df.columns[4:]    
    for column in df.iloc[:,4:]:
        all_dates[column] = df[column].sum()
    return pd.Series(all_dates)

def graph(df, line_dir):
    plt.clf()
    line_grh = df.plot(kind="line", y="Deaths", x ="Date", figsize=(12, 8))
    line_grh2 = df.plot(kind="line", y="Cases", x ="Date", figsize=(12, 8))
    plt.yscale("log")
    plt.savefig(line_dir)
    