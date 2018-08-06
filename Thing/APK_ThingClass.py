import Thing


class APK_ThingClass(Thing.ThingClass):
    """ Base Class for Things"""

    def __init__(self, TID, tr):
        Thing.ThingClass.__init__(self, TID, tr)
        return

    def get_topics(self):
        return

    def on_message(self):
        return

    def process(self):
        return

    def cleanup(self):
        return


