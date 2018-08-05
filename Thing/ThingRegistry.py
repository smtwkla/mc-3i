class ThingRegistryClass:
    """ Base Class for Things Registry"""

    def __init__(self, dbc, mqtt):
        self.DBC = dbc
        self.MQTT = mqtt
