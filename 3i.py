
import mqtt_config as mqtt_c
import topic_config as topic_c
import DBC as dbc
import Rule as RuleClass
import MQTTHandlerClass


# Create Database Class
db = dbc.DBConnector()

# Connect to Database
db.connect()

# Load Topics List from JSON File
topic = topic_c.read_topic_conf()

RuleList = []

# Parse Topics to be subscribed to from JSON File and add it to RuleList[]
for aTopic in topic.items():
    r = RuleClass.Rule(db, name=aTopic[0], topic=aTopic[1]['TOPIC'],
                       tablename=aTopic[1]['TABLE'], insert=aTopic[1]['INSERT'])
    RuleList.append(r)

print(str(len(RuleList)) + " topic rules added.")



# Load MQTT Server Config from JSON File
conf = mqtt_c.read_mqtt_conf()

print("MQTT Server Config:")
print(conf['mqtt_host'] + ":" + str(conf['mqtt_port']) + " " + conf['mqtt_username'] + " " + conf['mqtt_password'])

mq = MQTTHandlerClass.MQTTHandlerClass()
mq.setRuleList(RuleList)

mq.connect_to_server(conf)

mq.client.loop_forever()
