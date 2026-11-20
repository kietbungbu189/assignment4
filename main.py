from src.config import CSV_D
from src.config import CSV_C
import pandas as pd
from src.extract import extract_csv
from src.analytics import aggregate_total

def main():
    deaths_df = extract_csv(CSV_D)
    cases_df = extract_csv(CSV_C)

    tot_d = aggregate_total(deaths_df)
    tot_c = aggregate_total(cases_df)

if __name__ == "__main__":
    main()

