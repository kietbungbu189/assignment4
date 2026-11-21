from datetime import datetime
#1 Record when an analysis occurs
from src.config import LOG

def log(log_dir):
    log_time = datetime.now()
    log_time = log_time.strftime("%h-%m-%s %m/%d/%y")
#index=False for pandas to_csv()
    with open(log_dir, mode="a") as lg:
        lg.write(log_time)
    