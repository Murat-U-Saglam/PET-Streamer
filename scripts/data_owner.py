import pandas as pd
from faker import Faker
import logging
from werkzeug.serving import WSGIRequestHandler
import json
from server import ServerGenerator

logger = logging.getLogger(__name__)

def generate_data(rows: int) -> pd.DataFrame:
    fake = Faker()
    data = {
        'Name': [fake.name() for _ in range(rows)],
        'Age': [fake.random_int(min=18, max=80) for _ in range(rows)],
        'Email': [fake.email() for _ in range(rows)],
        'Address': [fake.address() for _ in range(rows)],
        'Phone': [fake.phone_number() for _ in range(rows)],
        "Gender": [fake.random_int(min=1, max=2) for _ in range(rows)], #1 male, 2 female
        "Alchol-use": [fake.random_int(min=1, max=2) for _ in range(rows)], #1 yes, 2 no
        "Air-pollution":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Diet-score":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Genetic-risk":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Dust-allergy":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Occupational-hazard":[fake.random_int(min=0, max=10) for _ in range(rows)]
    }
    df = pd.DataFrame(data)
    logger.info("Generated data")
    return (df)

def run_server(df: pd.DataFrame) -> None:
    configuration = json.load(open("configs/metadata_catalogue.json"))    
    ServerGenerator(5000, "Data Owner").set_endpoint("data", {"headers": configuration["headers"],
                       "requires_anonymisation": configuration["requires_anonymisation"],
                       "requires_psuedonimisation": configuration["requires_psuedonimisation"],
                        "data": df.to_dict(orient="records")})

def main():    
    rows = 5
    df = generate_data(rows)
    run_server(df)