import logging



class ShadowEngineClass:

    SHADOW_TYPE_INT = 0
    SHADOW_TYPE_STR = 1
    SHADOW_TYPE_FLOAT = 2

    def __init__(self, env):
        self.env = env
        self.shadow_table = "Shadows"

    def update_shadow(self, tid, shadow_prop, data_type, val):
        dbc = self.env.dbc

        record = {}

        if data_type == self.SHADOW_TYPE_STR:
            record["value_s"] = val

        elif data_type == self.SHADOW_TYPE_INT:
            record["value_i"] = val

        elif data_type == self.SHADOW_TYPE_FLOAT:
            record["value_f"] = val

        else:
            logging.critical(f"Error : Unknown Shadow Data Type {data_type}")
            return False

        condition = f"tid='{tid}' AND property='{shadow_prop}'"
        dbc.update(self.shadow_table, record, condition)



