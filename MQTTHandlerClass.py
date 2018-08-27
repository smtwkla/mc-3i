import paho.mqtt.client as mqtt
import logging

class MQTTHandlerClass(object):
    def __init__(self, env):
        self.client = None
        self.conf = None
        self.env = env
        super(MQTTHandlerClass, self).__init__()

    def setRuleList(self, rl):
        self.RuleList = rl

    def connect_to_server(self, conf):
        self.conf = conf

        # MQTT paho Client
        self.client = mqtt.Client(client_id=conf['client_id'], clean_session=False)

        if conf['mqtt_username'] != '':
            self.client.username_pw_set(conf['mqtt_username'], conf['mqtt_password'])

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Connect to MQTT Server
        self.client.connect(conf['mqtt_host'], conf['mqtt_port'], 60)

    def on_connect(self, client, userdata, flags,rc):
        logging.info("Connected with result code "+str(rc))
    # Subscribe to all rule topics defined in RuleList
        for aRule in self.RuleList:
            client.subscribe(aRule.getTopic())

    def on_message(self, client, userdata, msg):
        # Find correct rule from RuleList
        # Pass message JSON Payload to Rule for action

        # Loop through RuleList and find if message topic applies
        for aRule in self.RuleList:
            if mqtt.topic_matches_sub(aRule.getTopic(), msg.topic):
                aRule.message_in(msg=msg)
                # print msg.payload
        # Call RuleList message_in method
