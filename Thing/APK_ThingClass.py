from Thing import ThingClass as Tc


class APK_ThingClass(Tc.ThingClass):
    """ Base Class for Things"""

    def __init__(self, TID, tr):
        Tc.ThingClass.__init__(self, TID, tr)
        return

    def get_topics(self):
        return

    def on_message(self):
        return

    def process(self):
        return

    def cleanup(self):
        return


