import json
from os import path

def read_mqtt_conf():
    with open(path.relpath('conf/mqtt_config.json'), 'r') as s:
        config = json.load(s)

    mqtt_host = config['MQTT']['HOST']
    mqtt_port = config['MQTT']['PORT']
    mqtt_username = config['MQTT']['USER']
    mqtt_password = config['MQTT']['PASS']
    return {'mqtt_host' : mqtt_host, 'mqtt_port' : mqtt_port, 'mqtt_username' : mqtt_username, 'mqtt_password' :mqtt_password}
