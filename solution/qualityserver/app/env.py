import os
import dotenv
import uuid

dotenv.load_dotenv()

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', "INFO").upper()
app_name = os.getenv('APP_NAME', "mythicalproductgrpc")
scope_keys = os.getenv('SCOPE_KEYS', "plant,edge,line,workload").split(",")
scope_values = os.getenv('SCOPE_VALUES', "FLOWERMOUND,MYTHICALNUC,FM407,QUALITYSERVER").split(",")   
prometheus_port = int(os.getenv("PROMETHEUS_PORT", "9600"))
scope_value_csv = ",".join(scope_values)
server_port = os.getenv("SERVER_PORT", "9001")


app_config={
    "app_name":app_name,
    "scope_keys":scope_keys,
    "scope_values":scope_values,
    "scope_value_csv":scope_value_csv,
    "logging_level":LOGGING_LEVEL,
    "prometheus_port":prometheus_port,
    "server_port":server_port
}

def get_config(key):
    if key in app_config:
        return app_config[key]
    elif key == "*":
        return app_config
    else:
        return None


def get_app_config(key):
    if key in app_config:
        return app_config[key]
    return app_config






