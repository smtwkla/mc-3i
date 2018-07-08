import json

with open('mqtt_config.json', 'r') as s:
    config = json.load(s)

mqtt_host = config['MQTT']['HOST'] # 'secret-key-of-myapp'
mqtt_port = config['MQTT']['PORT'] # 'web-hooking-url-from-ci-service'
mqtt_username = config['MQTT']['USER']
mqtt_password = config['MQTT']['PASS']

print "config:"
print mqtt_host + " " + mqtt_port + " " +  mqtt_username + " " + mqtt_password
