import pandas as pd
import numpy as np
from datetime import datetime

def convert_date(date):
    x = datetime.strclf(date)
    data = x("%H-%M-%S %m %d %y")
    return data

