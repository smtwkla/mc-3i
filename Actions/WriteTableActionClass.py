import Actions
import json as js
import logging

class WriteTableActionClass(Actions.RuleActionClass):

    def __init__(self, env, insert, tablename):
        self.env = env
        self.insert = insert
        self.tablename = tablename

    def on_message(self, msg):
        # decode JSON payload
        pl = msg.payload.decode("utf-8")
        logging.debug("Payload:  " + pl)
        jss = js.loads(pl)

        if self.insert:
            # INSERT SQL Statement
            self.env.dbc.insert(self.tablename, jss)

        else:
            # UPDATE SQL Statement - NOT YET IMPLEMENTED
            self.env.dbc.update()
        # UPDATE TableTouchCount

