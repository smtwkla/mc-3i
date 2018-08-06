import Read_Config as read_c
import DBC as dbc
import Rule as RuleClass
import MQTTHandlerClass
import Env3iClass
import Actions
import Thing

# Create App Class
Env3i = Env3iClass.Env3iClass()

# Create Database Class
Env3i.dbc = dbc.DBConnector()
# Connect to Database
Env3i.dbc.connect()

# Load Topics List from JSON File
topic = read_c.read_topic_conf()

Env3i.rules = []

# Parse Topics to be subscribed to from JSON File and add it to RuleList[]
for aTopic in topic.items():
    w = Actions.WriteTableActionClass(Env3i, aTopic[1]['INSERT'], aTopic[1]['TABLE'])
    r = RuleClass.Rule(name=aTopic[0], topic=aTopic[1]['TOPIC'], rule_action=w)
    Env3i.rules.append(r)

# Load Things

Env3i.tr = Thing.ThingRegistryClass(Env3i)
conf = read_c.read_things_conf()
Env3i.tr.load_things(conf)

# Load Rule Subscriptions of Things
for th in Env3i.tr.Things:
    print("Loaded device ", th.get_tid())
    top = th.get_topics()
    print("Needs ", top)
    if top is None:
        pass
    else:
        r = RuleClass.Rule(name=th.get_tid()+":"+top, topic=top, rule_action=th)
        Env3i.rules.append(r)

print(str(len(Env3i.rules)) + " topic rules added.")

# Load MQTT Server Config from JSON File
conf = read_c.read_mqtt_conf()

print("MQTT Server Config:")
print(conf['mqtt_host'] + ":" + str(conf['mqtt_port']) + " " + conf['mqtt_username'] + " " + conf['mqtt_password'])

Env3i.mqtt = MQTTHandlerClass.MQTTHandlerClass()
Env3i.mqtt.setRuleList(Env3i.rules)
Env3i.mqtt.connect_to_server(conf)
Env3i.mqtt.client.loop_forever()



