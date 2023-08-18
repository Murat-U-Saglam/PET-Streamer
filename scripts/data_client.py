import requests 
import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def check_connection(url: str) -> bool:
    try:
        requests.get(url)
        return True
    except:
        logger.error("Could not connect to server")
        return False
    
def get_data(url: str) -> dict:
    response = requests.get(url)
    data = response.json()
    logger.info("Received data")
    return data

