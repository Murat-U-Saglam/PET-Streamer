import data_client
import api
import data_owner
import sys
import logging
import logging.config
import threading
import time

def main():
    background_thread = threading.Thread(target=data_owner.main)
    background_thread.start()
    time.sleep(1)
    api.main()
    

if __name__ == "__main__":
    logging.config.fileConfig('configs/logging.conf')
    main()