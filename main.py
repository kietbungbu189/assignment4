from src.config import CSV_D
from src.config import CSV_C
import pandas as pd
from src.extract import extract_csv
from src.analytics import aggregate_total
from src.transform import convert_date
from src.config import TARGET_FILEORADDRESS
from src.extract import av_extract
from src.log import log
from src.config import LOG

def main():
    deaths_df = extract_csv(CSV_D)
    cases_df = extract_csv(CSV_C)

    tot_d = aggregate_total(deaths_df)
    tot_c = aggregate_total(cases_df)

    dt_list_d = {}
#because all_dates is dict inside aggregate_total() so change...
#... enumerate() (for list) to .items() for dict (or Series...
#... when it's converted at "return"
    for key, value in tot_d.items():
        d = convert_date(key)
#use this instead of dt_list_d.append(d: value) to include...
#... deaths/cases values with the dates
        dt_list_d[d] = value
    print(dt_list_d)

    dt_list_c = {}
    for key2, value2 in tot_c.items():
        d2 = convert_date(key2)
        dt_list_c[d2] = value2
    print(dt_list_c)

    alpha_vantage = av_extract(TARGET_FILEORADDRESS)

    log(LOG)

if __name__ == "__main__":
    main()

