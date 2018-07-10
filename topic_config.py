import json
from os import path

def read_topic_conf():
    with open(path.relpath('conf/topic_config.json'), 'r') as s:
        config = json.load(s)
    return config
