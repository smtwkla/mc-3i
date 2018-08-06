

class ThingClass:
    """ Base Class for Things"""

    def __init__(self, TID, env):
        self.__TID = TID
        self.env = env

    def get_tid(self):
        return self.__TID

    def get_topics(self):
        return None

    def on_message(self, msg):

        return

    def process(self):
        return

    def cleanup(self):
        return


