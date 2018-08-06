#from Thing import ThingClass as t
#tc = t.ThingClass("LF1", None, None)
#print(tc.get_tid())

import Thing
import mqtt_config as mqtt_c

tr = Thing.ThingRegistryClass(None, None)
conf = mqtt_c.read_things_conf()
tr.load_things(conf)

for th in tr.Things:
    print(th.get_tid())
