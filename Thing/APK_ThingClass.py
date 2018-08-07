import Thing


class APK_ThingClass(Thing.ThingClass):
    """ Machine Specific Thing Class for Automatic Packing Machine """

    def __init__(self, TID, env):
        Thing.ThingClass.__init__(self, TID, env)
        return

    def get_topics(self):
        t = self.env.topic_root + self.get_tid()
        return t

    def on_message(self, msg):
        pl = msg.payload.decode("utf-8")
        print("Automatic Packing Machine " + self.get_tid() + " sent message: " + pl)
        return

    def process(self):
        return

    def cleanup(self):
        return


