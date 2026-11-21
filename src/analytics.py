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

def graph(df, line_dir, line_dir2):
    plt.clf()
    line_grh = df.plot(kind="line", y=["High", "Low"], x ="Date", figsize=(12, 8))
    plt.yscale("log")
    plt.title("Apple (AAPL) stock price high and low overtime")
    plt.savefig(line_dir)

#Dual-plot to show stock price more clear
    plt.clf()
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(df["Date"], df["Cases"], color="tab:orange", label="Cases")
    ax1.plot(df["Date"], df["Deaths"], color="tab:blue", label="Deaths")

    ax1.set_yscale("log")
    ax1.set_ylabel("COVID Cases & Deaths (Log Scale)")
    ax1.set_xlabel("Date")

    ax2 = ax1.twinx()

    ax2.plot(df["Date"], df["Close"], color="tab:green", label="Stock Close Price")
    ax2.set_ylabel("Stock Close Price ($)", color="tab:green")

    plt.title("COVID-19 vs. Stock Close Price")

# 1. Grab the line styles and labels from the left axis (Cases, Deaths)
    lines_1, labels_1 = ax1.get_legend_handles_labels()

# 2. Grab the line style and label from the right axis (Stock Close Price)
    lines_2, labels_2 = ax2.get_legend_handles_labels()

# 3. Combine both lists and draw one legend box in the top-left corner
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")


    plt.savefig(line_dir2)
