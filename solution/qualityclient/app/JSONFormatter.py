import logging
import json
from datetime import datetime
from datetime import timezone
import time

class JSONFormatter(logging.Formatter):

    def __init__(self):
        super().__init__()

    def format(self, record):
        obj_to_dump = {}
        utc_time = datetime.fromtimestamp(record.created,tz=timezone.utc)
        obj_to_dump["timestamp"] = str(utc_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
        obj_to_dump["msg"] = record.msg
        obj_to_dump["levelname"] = record.levelname
        obj_to_dump["funcName"] = record.funcName
        obj_to_dump["filename"] = record.filename
        obj_to_dump["module"] = record.module
        obj_to_dump["name"] = record.name
        obj_to_dump["scope"] = record.scope
        record.msg = json.dumps(obj_to_dump)
        return super().format(record)