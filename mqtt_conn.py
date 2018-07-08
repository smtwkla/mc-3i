
import paho.mqtt.client as mqtt
import mqtt_config

conf=mqtt_config.read_mqtt_conf()

print "config:"
print conf['mqtt_host'] + " " + str(conf['mqtt_port']) + " " +  conf['mqtt_username'] + " " + conf['mqtt_password']


def on_connect(client, userdata, flags,rc):
	print("Connected with result code "+str(rc))
	client.subscribe("test")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.username_pw_set(conf['mqtt_username'],conf['mqtt_password'])
client.on_connect = on_connect
client.on_message = on_message

client.connect(conf['mqtt_host'], conf['mqtt_port'], 60)

client.loop_forever()
