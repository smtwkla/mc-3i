import json
from os import path


def read_mqtt_conf(conf):
    with open(path.relpath(conf + '/mqtt_config.json'), 'r') as s:
        config = json.load(s)

    mqtt_host = config['MQTT']['HOST']
    mqtt_port = config['MQTT']['PORT']
    mqtt_username = config['MQTT']['USER']
    mqtt_password = config['MQTT']['PASS']
    mqtt_topic_root = config['IOT_SITE']['TOPIC_ROOT']
    mqtt_client_id = config['IOT_SITE']['CLIENT_ID']

    return {'mqtt_host': mqtt_host, 'mqtt_port': mqtt_port, 'mqtt_username': mqtt_username,
            'mqtt_password': mqtt_password, 'topic_root': mqtt_topic_root, 'client_id': mqtt_client_id}


def read_things_conf(conf):
    with open(path.relpath(conf + '/things_config.json'), 'r') as s:
        config = json.load(s)

    return config


def read_direct2db_topic_conf(conf):
    with open(path.relpath(conf + '/direct2db_config.json'), 'r') as s:
        config = json.load(s)
    return config
