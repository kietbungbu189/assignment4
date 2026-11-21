import pandas as pd
import numpy as np
from datetime import datetime

def convert_date(date):
#use strptime (date type -> text) instead of strftime (text...
#... -> date type)
    x = datetime.strptime(date)
    data = x("%H-%M-%S %m %d %y")
    return data

