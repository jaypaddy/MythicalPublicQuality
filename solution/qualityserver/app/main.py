import time
import logging
import logging.config
from datetime import datetime
import json
import uuid

import os
from metrics import start_metrics_server, reqmetric, tempmetric, pressuremetric
from env import get_config, scope_values
from JSONFormatter import JSONFormatter
from concurrent import futures

from flask import Flask, jsonify
import random

#: Init our logger
logger=logging.getLogger()


app = Flask(__name__)


@app.route("/")
def root():
    reqmetric.inc(labels=scope_values) 
    return "Hello World!"

@app.route("/GetQuality")
def GetQuality():
    reqmetric.inc(labels=scope_values) 
    response = {"statuscode":200,"quality":"good","timestamp":datetime.now().isoformat()}
    # Simulate some Metrics
    tempmetric.set(random.randint(1000,5000), get_config('scope_values'))
    pressuremetric.set(random.randint(1,100), get_config('scope_values'))

    return jsonify(response)

def run_sample():  
    app.run(host='0.0.0.0',port=get_config("server_port")) 
    return


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