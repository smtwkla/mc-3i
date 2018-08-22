import Thing
from ShadowEngine import ShadowEngineClass


class LiftThingClass(Thing.ThingClass):
    """ Machine Specific Thing Class for Generic Lift """

    def __init__(self, TID, env):
        Thing.ThingClass.__init__(self, TID, env)
        self.def_table = "LiftData"
        self.shadow_table = "Shadows"
        return

    def get_topics(self):
        t = self.env.topic_root + self.get_tid()
        return t

    def on_message(self, msg):
        pl = msg.payload.decode("utf-8")
        print("Lift " + self.get_tid() + " sent message: " + pl)

        data = pl.split()
        ts = data[0]
        msg = data[1].upper()
        tid = self.get_tid()
        i_val = 0
        s_val = ""
        f_val = 0.0

        if msg == "UP":
            f_val = data[2]

        elif msg == "DOWN":
            f_val = data[2]

        elif msg == "OLR_TRIP":
            shadow = "Status"
            shadow_t = ShadowEngineClass.SHADOW_TYPE_STR
            shadow_s = "TRIP"
            self.env.se.update_shadow(tid, shadow, shadow_t, shadow_s)

        elif msg == "OLR_RESET":
            shadow = "Status"
            shadow_t = ShadowEngineClass.SHADOW_TYPE_STR
            shadow_s = "Ok"
            self.env.se.update_shadow(tid, shadow, shadow_t, shadow_s)

        table = self.def_table

        record = {"tid": tid, "event_time": ts, "event_type": msg, "event_data_i": i_val, "event_data_s": s_val, \
                  "event_data_f": f_val}

        self.env.dbc.insert(table, record)

        return

    def process(self):
        return

    def cleanup(self):
        return


