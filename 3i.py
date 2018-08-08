import Read_Config as read_c
import DBC as dbc
import Rule as RuleClass
import MQTTHandlerClass
import Env3iClass
import RuleRegister
import Actions
import Thing
import sys
from CmdArgParse import process_args
import logging

# Create App Class
Env3i = Env3iClass.Env3iClass()

# Set defaults
Env3i.db_conf = "conf/"
Env3i.conf_root = "conf/"

l_filename = None
l_level = logging.INFO

# Process command line arguments
if len(sys.argv) >= 1:
    (switches, flags) = process_args(sys.argv)
    for i in switches:
        if i[0] == "-d":
            Env3i.db_conf = str(i[1])
        elif i[0] == "-c":
            Env3i.conf_root = i[1]
        elif i[0] == "-L":
            if i[1].strip().upper() == "DEBUG":
                l_level = logging.DEBUG
        elif i[0] == "-LF":
            l_filename = i[1]
        else:
            logging.critical("Error : Unknown command line switch " + i[0])
            exit(1)
    for i in flags:
        if "MODE_ACTION" == i.strip().upper():
            Env3i.action_daemon_mode = True
        else:
            logging.critical("Error : Unknown command line flag " + i)
            exit(1)

# Configure Logger
FORMAT = '%(asctime)-15s : %(levelname)s : %(module)s : %(message)s'
logging.basicConfig(format=FORMAT, filename=l_filename, level=l_level)

logging.info("DB Conf path: " + Env3i.db_conf)
logging.info("Conf Root path: " + Env3i.conf_root)

# Create Database Class
Env3i.dbc = dbc.DBConnector(Env3i.conf_root)
# Connect to Database
Env3i.dbc.connect()

# Load MQTT Server Config from JSON File
m_conf = read_c.read_mqtt_conf(Env3i.conf_root)

logging.info("MQTT Server Config: " + m_conf['mqtt_host'] + ":" + str(m_conf['mqtt_port']) + " " + m_conf['mqtt_username'] + " " + m_conf['mqtt_password'] + " " + m_conf['topic_root'])

Env3i.topic_root = m_conf['topic_root']
Env3i.rules = []

if Env3i.action_daemon_mode:

    logging.info("Starting in Action Rule Mode...")

    Env3i.rr = RuleRegister.RuleRegisterClass(Env3i)

    sql_fld = "3i_Rules.RuleName, 3i_Rules.RuleID, 3i_Rules.Topic, 3i_Rules.Operation, 3i_Rules.TableName, 3i_Rules.last_modified"
    sql_where = "3i_Rules.Enabled = TRUE"
    res = Env3i.dbc.select("3i_Rules", sql_fld, condition=sql_where, group_by=None, limit="1000")
    rule_res = res.fetchall()

    # Parse Direct Table Write Action Topics to be subscribed to from JSON File and add it to RuleList[]
    for aTopic in rule_res:
        print(aTopic)
        w = Actions.WriteTableActionClass(Env3i, aTopic['Operation'], aTopic['TableName'])
        r = RuleClass.Rule(name=aTopic['RuleName'], topic=aTopic['Topic'], rule_action=w, time_stamp=['last_modified'])
        Env3i.rr.add_rule(r)
else:
    # Load Things

    Env3i.tr = Thing.ThingRegistryClass(Env3i)
    conf = read_c.read_things_conf(Env3i.conf_root)
    Env3i.tr.load_things(conf)

    # Load Rule Subscriptions of Things
    for th in Env3i.tr.Things.keys():
        tid = Env3i.tr.Things[th].get_tid()
        top = Env3i.tr.Things[th].get_topics()
        logging.info("Loaded device " + tid  + ", needs ", top)
        if top is None:
            pass
        else:
            r = RuleClass.Rule(name=tid+":"+top, topic=top, rule_action=Env3i.tr.Things[th])
            Env3i.rules.append(r)

logging.info(str(len(Env3i.rr.rules)) + " topic rules added.")

Env3i.mqtt = MQTTHandlerClass.MQTTHandlerClass()
Env3i.mqtt.setRuleList(Env3i.rr.rules)
Env3i.mqtt.connect_to_server(m_conf)
Env3i.mqtt.client.loop_forever()


