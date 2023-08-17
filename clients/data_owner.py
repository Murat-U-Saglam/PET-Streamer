import pandas as pd
from faker import Faker
import random
from flask import Flask, jsonify

def generate_data(rows: int) -> pd.DataFrame:
    fake = Faker()
    data = {
        'Name': [fake.name() for _ in range(rows)],
        'Age': [fake.random_int(min=18, max=80) for _ in range(rows)],
        'Email': [fake.email() for _ in range(rows)],
        'Address': [fake.address() for _ in range(rows)],
        'Phone': [fake.phone_number() for _ in range(rows)],
        "Gender": [random.choice(["male", "female"]) for _ in range(rows)],
        "Alchol-use": [random.choice(["yes", "no"]) for _ in range(rows)],
        "Air-pollution":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Diet-score":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Genetic-risk":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Dust-allergy":[fake.random_int(min=0, max=10) for _ in range(rows)],
        "Occupational-hazard":[fake.random_int(min=0, max=10) for _ in range(rows)]
    }
    df = pd.DataFrame(data)
    return (df)

def run_server():
    rows = 100
    app = Flask(__name__)
    df = generate_data(rows)
    @app.route('/data')
    def get_data():
        return jsonify(df.to_dict(orient="records"))
    app.run()

