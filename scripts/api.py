import requests 
import json
import pandas as pd
import numpy as np
import logging
import anonymiser
import http.server
import socketserver

logger = logging.getLogger(__name__)

class JSONRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, variable, *args, **kwargs):
        self.variable = variable
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Convert the Python dictionary to JSON and send it as response
            response_data = json.dumps(self.variable).encode('utf-8')
            self.wfile.write(response_data)
        else:
            # Serve other files using the default behavior
            super().do_GET()



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

def main():
    url = "http://127.0.0.1:5000/data"
    if not check_connection(url):
        logger.error("Could not connect to server")
        exit(1)
    data = get_data(url)
    df = pd.DataFrame(data["data"])
    configuration = json.load(open("configs/metadata_catalogue.json"))
    df = anonymiser.anonymise(df, configuration)
    json_data = df.to_json(orient="records")
    handler_with_variable = lambda *args, **kwargs: JSONRequestHandler(json_data, *args, **kwargs)
    
    with socketserver.TCPServer(('', 8001), handler_with_variable) as httpd:
        print(f"Serving at port {8001}")
        httpd.serve_forever()

