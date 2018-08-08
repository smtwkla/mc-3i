import Read_Config as read_c
import DBC as dbc
import Rule as RuleClass
import MQTTHandlerClass
import Env3iClass
import Actions
import Thing
import sys
from CmdArgParse import process_args

# Create App Class
Env3i = Env3iClass.Env3iClass()

# Set defaults
Env3i.db_conf = "conf/"
Env3i.conf_root = "conf/"

# Process command line arguments
if len(sys.argv) >= 1:
    (switches, flags) = process_args(sys.argv)
    for i in switches:
        if i[0] == "-d":
            Env3i.db_conf = i[1]
        elif i[0] == "-c":
            Env3i.conf_root = i[1]

print("DB Conf:", Env3i.db_conf)
print("Conf Root:", Env3i.conf_root)

# Create Database Class
Env3i.dbc = dbc.DBConnector(Env3i.conf_root)
# Connect to Database
Env3i.dbc.connect()

# Load MQTT Server Config from JSON File
m_conf = read_c.read_mqtt_conf(Env3i.conf_root)

print("MQTT Server Config:")
print(m_conf['mqtt_host'] + ":" + str(m_conf['mqtt_port']) + " " + m_conf['mqtt_username'] + " " + m_conf['mqtt_password'] + " " + m_conf['topic_root'])

Env3i.topic_root = m_conf['topic_root']

# Load Direct2DB Topics List from JSON File
topic = read_c.read_direct2db_topic_conf(Env3i.conf_root)

Env3i.rules = []

# Parse Direct Table Write Action Topics to be subscribed to from JSON File and add it to RuleList[]
for aTopic in topic.items():
    if aTopic[0] == "//":
        pass  # Ignore comment in JSON file
    else:
        w = Actions.WriteTableActionClass(Env3i, aTopic[1]['INSERT'], aTopic[1]['TABLE'])
        r = RuleClass.Rule(name=aTopic[0], topic=aTopic[1]['TOPIC'], rule_action=w)
        Env3i.rules.append(r)

# Load Things

Env3i.tr = Thing.ThingRegistryClass(Env3i)
conf = read_c.read_things_conf(Env3i.conf_root)
Env3i.tr.load_things(conf)

# Load Rule Subscriptions of Things
for th in Env3i.tr.Things.keys():
    tid=Env3i.tr.Things[th].get_tid()
    print("Loaded device ", tid)
    top = Env3i.tr.Things[th].get_topics()
    print("Needs ", top)
    if top is None:
        pass
    else:
        r = RuleClass.Rule(name=tid+":"+top, topic=top, rule_action=Env3i.tr.Things[th])
        Env3i.rules.append(r)

print(str(len(Env3i.rules)) + " topic rules added.")


Env3i.mqtt = MQTTHandlerClass.MQTTHandlerClass()
Env3i.mqtt.setRuleList(Env3i.rules)
Env3i.mqtt.connect_to_server(m_conf)
Env3i.mqtt.client.loop_forever()



