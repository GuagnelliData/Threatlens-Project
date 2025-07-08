import pandas as pd
from . import config

def load_data(path=config.CSV_FILE):
    print(f"📦 Loading dataset from: {path}")
    df = pd.read_csv(path)
    return df
