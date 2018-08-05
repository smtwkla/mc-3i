
class ThingClass:
    """ Base Class for Things"""

    def __init__(self, TID, dbc, mqtt):
        self.TID = TID
        self.DBC = dbc
        self.MQTT = mqtt

    def get_tid(self):
        return self.TID

    def get_topics(self):
        return ""

    def on_message(self):
        return

    def process(self):
        return

    def cleanup(self):
        return


