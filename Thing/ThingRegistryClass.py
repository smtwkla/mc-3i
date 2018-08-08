import Thing
import logging

class ThingRegistryClass:
    """ Base Class for Things Registry"""

    def __init__(self, env):
        self.env = env
        self.Things = {}  # Things List

    def load_things(self, thingslist):
        for thing in thingslist.items():

            logging.info("Processing %s : Class %s..." % (thing[1]["TID"], thing[1]["CLASS"]))

            thing_class = thing[1]["CLASS"]
            tid = thing[1]["TID"]
            obj = None

            if thing_class == "APK_ThingClass":
                obj = Thing.APK_ThingClass(tid, self.env)

            elif thing_class == "SAPK_ThingClass":
                obj = Thing.ThingClass(tid, self.env)

            elif thing_class == "ThingClass":
                obj = Thing.ThingClass(tid, self.env)

            if obj is None:
                logging.error("Error : Unknown Class %s." % thing_class)

            else:
                # Append Thing to Things list
                self.Things[tid] = obj

        return

    def get_thing(self, tid):
        #  Find Thing Object
        return self.Things[tid]
        pass
