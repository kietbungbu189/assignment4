from src.config import CSV_D
from src.config import CSV_C
import pandas as pd
from src.extract import extract_csv
from src.analytics import aggregate_total
from src.transform import convert_date
from src.config import TARGET_FILEORADDRESS
from src.extract import av_extract
from src.log import log
from src.config import LOG_DIR
from src.config import TEST_PRINT
import json
from src.transform import flatten_data
#stock used = AAPL, yahoo finance is used instead of Alp Advtg...
#... , legacy code of requests commented out
from src.config import TEST_PRINT2
import yfinance as yf
from src.config import TEST_PRINT3
from src.config import TICKER
from src.config import CSV

def main():
    deaths_df = extract_csv(CSV_D)
    cases_df = extract_csv(CSV_C)

    tot_d = aggregate_total(deaths_df)
    tot_c = aggregate_total(cases_df)

    dt_dict_d = {}
#because all_dates is dict inside aggregate_total() so change...
#... enumerate() (for list) to .items() for dict (or Series...
#... when it's converted at "return"
    for key, value in tot_d.items():
        d = convert_date(key)
#use this instead of dt_list_d.append(d: value) to include...
#... deaths/cases values with the dates
        dt_dict_d[d] = value
    print(dt_dict_d)

    dt_dict_c = {}
    for key2, value2 in tot_c.items():
        d2 = convert_date(key2)
        dt_dict_c[d2] = value2
    print(dt_dict_c)

#.T to transpose from rows into columns
    a_dataframe_that_aggregates = pd.DataFrame([dt_dict_d, dt_dict_c]).T
#the header (or promoted row 0 in csv) becomes...
#... "index" column, then row[0] becomes "0" and...
#... row[1] becomes "1"    
    a_dataframe_that_aggregates = a_dataframe_that_aggregates.rename(columns={"index": "date", 0: "Deaths", 1: "Cases"})
    print(a_dataframe_that_aggregates.head())

    with open(TEST_PRINT3, mode="a") as ts3:
        a_dataframe_that_aggregates.to_csv(ts3)
    
    alpha_vantage = av_extract(TARGET_FILEORADDRESS, TICKER)

    with open(TEST_PRINT, mode="a") as ts:
#        ts.write(alpha_vantage)
#pass indent=4 to format the data for human eye
        json.dump(alpha_vantage, ts, indent=4)

    flat = flatten_data(alpha_vantage)
    print(flat.head())
    with open (TEST_PRINT2, mode="a") as ts2:
        flat.to_csv(ts2)

    start_idx = 0
    end_idx = (len(a_dataframe_that_aggregates.iloc[:,0])-1)
# By Column and Row - HP of a Plymouth Satellite
#    df.iloc[2,3] or df.loc[[1], ['name']]
#In your dataframe, the dates are still the row index, and...
#... df.iloc[:, 0] is the Deaths column. Calling .index...
#retrieves the index of the whole row ([0]) instead of...
#... the name of the index 
    start = a_dataframe_that_aggregates.iloc[start_idx].name
    end = a_dataframe_that_aggregates.iloc[end_idx].name
#(start / end): YYYY-MM-DD strings or datetime...
#... objects (start is inclusive, end is exclusive)
#    end = end+1
    end = end + pd.Timedelta(days=1)
    AAPL_stk = yf.download(TICKER, start, end)

#    selected_orders = selected_orders.merge(
#        material_restock[["SKU", "Quantity to order"]],
#        on="SKU",
#        how="left",
#        validate="many_to_one"
#    )
    covid_vs_stk = AAPL_stk.merge(
        a_dataframe_that_aggregates[["Deaths", "Cases"]],
        on="Date",
        how="left",
        validate="one_to_one"
    )

#    with open(CSV, mode="a") as dt:
#        AAPL_stk.to_csv(dt)

    log(LOG_DIR)

if __name__ == "__main__":
    main()

