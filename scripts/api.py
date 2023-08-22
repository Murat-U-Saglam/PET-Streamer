import requests 
import json
import pandas as pd
import numpy as np
import logging
import anonymiser
from server import ServerGenerator, get_data

logger = logging.getLogger(__name__)

def check_connection(url: str) -> bool:
    try:
        requests.get(url)
        return True
    except:
        logger.error("Could not connect to server")
        print("Data source cannot be connected to")
        exit(1)
    


def run_server(df: pd.DataFrame) -> None:
    ServerGenerator(5001, "Anonymised_Data").set_endpoint("data", {"data": df.to_dict(orient="records")})

def main():
    url = "http://127.0.0.1:5000/data"
    if not check_connection(url):
        logger.error("Could not connect to server")
    data = get_data(url)
    df = pd.DataFrame(data["data"])
    configuration = {
        "headers": data["headers"],
        "requires_anonymisation": data["requires_anonymisation"],
        "requires_psuedonimisation": data["requires_psuedonimisation"]
        }
    df = anonymiser.anonymise(df, configuration)
    json_data = df.to_json(orient="records")
    run_server(df)