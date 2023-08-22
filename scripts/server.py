from flask import Flask, jsonify
import json
import pandas as pd
import logging
from werkzeug.serving import WSGIRequestHandler
import requests

logger = logging.getLogger(__name__)

class ServerGenerator:
    def __init__(self, port:int, name:str):
        """

        Args:
            port (int): Port number to run server on
            name (str): For logging purposes
        """
        self.port = port
        self.name = name

    
    def set_endpoint(self, subdir: str, data: dict) -> None:
        app = Flask(__name__)
        werkzeug_logger = logging.getLogger('werkzeug')
        werkzeug_logger.setLevel(logging.ERROR)  # Adjust as needed
        @app.route(f'/{subdir}')
        def get_data():
            return jsonify(data)
        logger.info(f"Starting '{self.name}' server")
        WSGIRequestHandler.handler_class = logging.NullHandler
        app.run(port=self.port ,debug=False)

def get_data(url: str) -> dict:
    response = requests.get(url)
    data = response.json()
    logger.info("Received data")
    return data