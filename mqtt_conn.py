
import paho.mqtt.client as mqtt
import mqtt_config as mqtt_c
import topic_config as topic_c

#Load MQTT Server Config from JSON File
conf=mqtt_c.read_mqtt_conf()

print "MQTT Server Config:"
print conf['mqtt_host'] + ":" + str(conf['mqtt_port']) + " " +  conf['mqtt_username'] + " " + conf['mqtt_password']

def on_connect(client, userdata, flags,rc):
	print("Connected with result code "+str(rc))
	client.subscribe("test")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

#Load Topics List from JSON File
topic=topic_c.read_topic_conf()

#Parse Topics to be subscribed to
for a in topic.items():
    print "Topic: "
    print a[1]['TOPIC']

#MQTT paho Client
client = mqtt.Client()
#client.username_pw_set(conf['mqtt_username'],conf['mqtt_password'])
client.on_connect = on_connect
client.on_message = on_message

#Connect to MQTT Server
client.connect(conf['mqtt_host'], conf['mqtt_port'], 60)


client.loop_forever()
