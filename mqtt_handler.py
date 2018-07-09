class mqtt_handler(object):
    def __init__(self):
        super(mqtt_handler, self).__init__()

    def setRuleList(self, rl):
        self.RuleList=rl

    def on_connect(self, client, userdata, flags,rc):
        print("Connected with result code "+str(rc))
    # Subscribe to all rule topics defined in RuleList
        for aRule in self.RuleList:
            client.subscribe(aRule.getTopic())

    def on_message(self, client, userdata, msg):
        # Find correct rule from RuleList
        # Pass message JSON Payload to Rule for writing to correct table

        #Loop through RuleList and find if message topic applies
        for aRule in self.RuleList:
            if (msg.topic==aRule.getTopic()):
                aRule.message_in(msg=msg)
        #Call RuleList message_in method