from src.config import CSV_D
from src.config import CSV_C
import pandas as pd
from src.extract import extract_csv
from src.analytics import aggregate_total
from src.transform import convert_date
from src.config import TARGET_FILEORADDRESS
from src.extract import av_extract

def main():
    deaths_df = extract_csv(CSV_D)
    cases_df = extract_csv(CSV_C)

    tot_d = aggregate_total(deaths_df)
    tot_c = aggregate_total(cases_df)

    dt_list_d = []
#because all_dates is dict inside aggregate_total() so change...
#... enumerate() (for list) to .items() for dict (or Series...
#... when it's converted at "return"
    for key, value in tot_d.items():
        d = convert_date(key)
        dt_list.append(d)
    print(dt_list_d)

    dt_list_c = []
    for key2, value2 in tot_c.items():
        d2 = convert_date(key2)
        dt_list_c.append(d2)
    print(dt_list_c)

    alpha_vantage = av_extract(TARGET_FILEORADDRESS)

if __name__ == "__main__":
    main()

