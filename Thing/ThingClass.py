

class ThingClass:
    """ Base Class for Things"""

    def __init__(self, TID, tr):
        self.__TID = TID
        self.TR = tr
        self.DBC = tr.DBC
        self.MQTT = tr.MQTT

    def get_tid(self):
        return self.__TID

    def get_topics(self):
        return

    def on_message(self, msg):

        return

    def process(self):
        return

    def cleanup(self):
        return


