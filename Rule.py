

class Rule(object):
    def __init__(self, name, topic, rule_action):
        self.name = name
        self.topic = topic
        self.rule_action = rule_action

    def getTopic(self):
        return self.topic

    def message_in(self, msg):
        # Process incoming MQTT Message
        print("Message arrived to Rule " + self.name + " : " + msg.topic + " " + str(msg.payload))
        self.rule_action.on_message(msg)
        return True


