import requests 
import json
import pandas as pd
import numpy as np

url = "http://127.0.0.1:5000//data"
def check_connection(str: url) -> bool:
    try:
        requests.get(url)
        return True
    except:
        return False
    
def get_data(url: str) -> pd.DataFrame:
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    if check_connection(url):
        df = get_data(url)
        print(df.head())
    else:
        print("Connection error")