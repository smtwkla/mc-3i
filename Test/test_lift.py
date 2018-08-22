from Thing import LiftThingClass
from Env3iClass import Env3iClass
import DBC
import datetime
import logging


class testmsg:
    def __init__(self):
        self.payload = ""


FORMAT = '%(asctime)-15s : %(levelname)s : %(module)s : %(message)s'
logging.basicConfig(format=FORMAT,  level=logging.DEBUG)


env = Env3iClass()
d = DBC.DBConnector(conf="../conf/")
d.connect()

env.dbc = d

lc = LiftThingClass("LIFT1", env)
msg = testmsg()

d = datetime.datetime.now()
tim = 5.5
cmd="UP"
print(d.isoformat())

msg.payload = f'{d.isoformat()} {cmd} {tim}'.encode("utf-8")
lc.on_message(msg)


