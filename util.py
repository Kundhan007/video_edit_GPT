import json


def read_config(con_file='../config.json'):
    with open(con_file, 'r') as f:
        config = json.load(f)
    return config
