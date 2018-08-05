import json as js


class Rule(object):
    def __init__(self, dbc, name, topic, tablename, insert):
        self.name = name
        self.dbc = dbc
        self.topic = topic
        self.tablename = tablename
        self.insert = insert

    def getTopic(self):
        return self.topic

    def message_in(self, msg):
        # Process incoming MQTT Message
        print("Message arrived to Rule " + self.name + " : " + msg.topic + " " + str(msg.payload))

        # decode JSON payload
        pl=msg.payload.decode("utf-8")
        print("Payload:  ")
        print(pl)
        jss = js.loads(pl)
        print(jss)

        if self.insert:
            # INSERT SQL Statement
            self.dbc.insert(self.tablename, jss)
        else:
            # UPDATE SQL Statement
            self.dbc.update()

        # UPDATE TableTouchCount
        return True

    # When message arrives, parse it, INSERT or UPDATE to table
