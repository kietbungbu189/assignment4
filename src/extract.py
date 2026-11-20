import pandas as pd

def extract_csv(csv_path):
    a = pd.read_csv(csv_path)
    return a
