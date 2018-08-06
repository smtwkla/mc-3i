from Thing import ThingClass as Tc
from Thing import APK_ThingClass as APKc

class ThingRegistryClass:
    """ Base Class for Things Registry"""

    def __init__(self, dbc, mqtt):
        self.DBC = dbc
        self.MQTT = mqtt
        self.Things = []  # Things List

    def load_things(self, thingslist):
        for thing in thingslist.items():

            print("Processing %s : Class %s..." % (thing[1]["TID"], thing[1]["CLASS"]))

            thing_class = thing[1]["CLASS"]
            tid = thing[1]["TID"]
            obj = None

            if thing_class == "APK_ThingClass":
                obj = APKc.APK_ThingClass(tid, self)

            elif thing_class == "SAPK_ThingClass":
                obj = Tc.ThingClass(tid, self)

            elif thing_class == "ThingClass":
                obj = Tc.ThingClass(tid, self)

            if obj is None:
                print("Error : Unknown Class %s." % thing_class)

            else:
                # Append Thing to Things list
                self.Things.append(obj)

        return
