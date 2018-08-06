#from Thing import ThingClass as t
#tc = t.ThingClass("LF1", None, None)
#print(tc.get_tid())

from Thing import ThingRegistryClass as trc
import mqtt_config as mqtt_c

tr = trc.ThingRegistryClass(None, None)
conf = mqtt_c.read_things_conf()
tr.load_things(conf)

for th in tr.Things:
    print(th.get_tid())
