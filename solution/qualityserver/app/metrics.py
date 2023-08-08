import logging
import threading
import time
import os

from datetime import datetime, timedelta
from prometheus_client import start_http_server, Counter, Gauge, Histogram
from env import scope_keys, scope_value_csv

logger = logging.getLogger()

class GaugeMetric:
    def __init__(self, name, description, labels):
        self.name = name
        self.description = description
        self.labels = labels
        self.gauge = Gauge(name, description, labels)

    def __str__(self):
        return f"{self.name} {self.description} {self.labels}"
    
    def set(self, value, labels=[]):
        self.gauge.labels(*labels).set(value)   

class CounterMetric:
    def __init__(self, name, description, labels):
        self.name = name
        self.description = description
        self.labels = labels
        self.counter = Counter(name, description, labels)

    def __str__(self):
        return f"{self.name} {self.description} {self.labels}"
    
    def inc(self, increment=1, labels=[]):
        self.counter.labels(*labels).inc(increment) 

def start_metrics_server(metrics_port):
    # Start up metrics scraper server
    start_http_server(metrics_port)
    logger.info(f"Metrics server started on port {int(metrics_port)}", extra={'scope': scope_value_csv})


reqmetric = CounterMetric("requestsserved", "Number of Requests served", scope_keys)
tempmetric = GaugeMetric("qs_temperature", "Temperature", scope_keys)
pressuremetric = GaugeMetric("qs_pressure", "Pressure", scope_keys)

