import json
import pandas as pd

import logging
logger = logging.getLogger(__name__)

def obfuscate(x: int) -> int:
    return x + 1

def anonymise(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    logger.info("Recieved data - Preparing to anonymise")
    headers = config["headers"]
    requires_anonymisation = config["requires_anonymisation"]
    requires_psuedonimisation = config["requires_psuedonimisation"]
    logger.info("Will be anonymising the following columns: {}".format(requires_anonymisation))
    logger.info("Will be psuedonimising the following columns: {}".format(requires_psuedonimisation))
    
    for column in requires_psuedonimisation:
        df[column] = df[column].apply(lambda x: obfuscate(x))

    for column in requires_anonymisation:
        df[column] = df[column].apply(lambda x: hash(x))

    logger.info("Anonymised data")
    return df

        




