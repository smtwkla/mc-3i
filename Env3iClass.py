import ShadowEngine

class Env3iClass:

    def __init__(self):
        self.dbc = None
        self.tr = None
        self.mqtt = None
        self.topic_root = ""
        self.conf_root = None
        self.db_conf = ""
        self.action_daemon_mode = False
        self.rr = None
        self.se = ShadowEngine.ShadowEngineClass(self)

    def quit_err(self):
        exit(1)

