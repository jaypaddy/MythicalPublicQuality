import time
import logging
import logging.config
from datetime import datetime
import json
import uuid
import requests

import os
from metrics import start_metrics_server, reqmetric, tempmetric, pressuremetric, egametric
from env import get_config, scope_values
from JSONFormatter import JSONFormatter
from concurrent import futures

import random


#: Init our logger
logger=logging.getLogger()




def run_sample():
    """ Run a loop that sleeps at random intervals and makes a http call to a server """
    while True:
        try:
            r = requests.get(get_config('server_method_url'))
            logging.info(f"Request made to {r.url} - {r.text}",extra={'scope': get_config('scope_value_csv')})
            reqmetric.inc(1, get_config('scope_values'))
            # Simulate some Metrics
            tempmetric.inc(1, get_config('scope_values'))
            pressuremetric.set(random.randint(80,100), get_config('scope_values'))
            egametric.set(random.randint(-5,5), get_config('scope_values'))

            time.sleep(get_config('sleep_interval_secs'))


        except KeyboardInterrupt:
            print ( "Server stopped" ) 
            break


def main():
    try:
        start_metrics_server(get_config('prometheus_port'))
        logging.info(f"Started {get_config('app_name')}",extra={'scope': get_config('scope_value_csv')})
        print(json.dumps(get_config("*"),indent=4))
        run_sample()
        
    except KeyboardInterrupt:
        print ( "Server stopped" ) 

if __name__ == "__main__":
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger()
    print(f"Setting Logging level to {get_config('logging_level').upper()} for all loggers")

    for handler in logger.handlers:
        handler.setLevel(get_config('logging_level').upper())
        #handler.setFormatter(JSONFormatter())
    main()