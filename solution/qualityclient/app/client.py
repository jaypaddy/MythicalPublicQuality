# using Mosquitto MQTT client, insert a set of data into a MQTT broker
import time
import logging
import logging.config
from datetime import datetime
import json
import uuid

import os
from metrics import start_metrics_server, submetric
from env import get_config, scope_values
from JSONFormatter import JSONFormatter
from concurrent import futures


import grpc

from protos import product_pb2_grpc
from protos import product_pb2
from google.protobuf.json_format import MessageToDict
from server import MythicalProductServiceServicer


with grpc.insecure_channel('10.0.0.29:50051') as channel:
    stub = product_pb2_grpc.MythicalProductServiceStub(channel)
    response = stub.GetCurrentProduct(product_pb2.Line(line="1"))
print (response)