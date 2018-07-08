import json

def read_topic_conf():
    with open('topic_config.json', 'r') as s:
        config = json.load(s)
    return config
