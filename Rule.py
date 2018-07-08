class Rule(object):
    def __init__(self, dbc, name, topic, tablename, insert):
        self.name=name
        self.dbc=dbc
        self.topic=topic
        self.tablename=tablename
        self.insert=insert

    def getTopic(self):
        return self.topic

    def message_in(self):
        #Process incomming MQTT Message
        return True

    # When message arrives, parse it, INSERT or UPDATE to table
