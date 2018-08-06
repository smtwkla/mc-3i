import mqtt_config as mqtt_c
import topic_config as topic_c
import DBC as dbc
import Rule as RuleClass
import MQTTHandlerClass
import Env3iClass
import Actions

# Create App Class
Env3i = Env3iClass.Env3iClass()

# Create Database Class
Env3i.dbc = dbc.DBConnector()
# Connect to Database
Env3i.dbc.connect()

# Load Topics List from JSON File
topic = topic_c.read_topic_conf()

Env3i.rules = []

# Parse Topics to be subscribed to from JSON File and add it to RuleList[]
for aTopic in topic.items():
    w = Actions.WriteTableActionClass(Env3i, aTopic[1]['INSERT'], aTopic[1]['TABLE'])
    r = RuleClass.Rule(name=aTopic[0], topic=aTopic[1]['TOPIC'], rule_action=w)
    Env3i.rules.append(r)

print(str(len(Env3i.rules)) + " topic rules added.")

# Load MQTT Server Config from JSON File
conf = mqtt_c.read_mqtt_conf()

print("MQTT Server Config:")
print(conf['mqtt_host'] + ":" + str(conf['mqtt_port']) + " " + conf['mqtt_username'] + " " + conf['mqtt_password'])

Env3i.mqtt = MQTTHandlerClass.MQTTHandlerClass()
Env3i.mqtt.setRuleList(Env3i.rules)
Env3i.mqtt.connect_to_server(conf)
Env3i.mqtt.client.loop_forever()



