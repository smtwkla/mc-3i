import logging

class Rule(object):
    def __init__(self, name, topic, rule_action):
        self.name = name
        self.topic = topic
        self.rule_action_obj = rule_action

    def getTopic(self):
        return self.topic

    def message_in(self, msg):
        # Process incoming MQTT Message
        logging.debug("Message arrived to Rule " + self.name + " topic " + msg.topic + " " + str(msg.payload))
        self.rule_action_obj.on_message(msg)
        return True


