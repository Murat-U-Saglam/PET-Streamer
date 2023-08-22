import data_client
import api
import data_owner
import sys
import logging
import logging.config
import threading
import time

def main():
    data_owner_server= threading.Thread(target=data_owner.main)
    data_owner_server.start()
    time.sleep(1)
    api_server = threading.Thread(target=api.main)
    api_server.start()
    

if __name__ == "__main__":
    logging.config.fileConfig('configs/logging.conf')
    main()