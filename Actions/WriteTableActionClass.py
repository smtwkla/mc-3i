import Actions
import json as js
import logging

class WriteTableActionClass(Actions.RuleActionClass):

    def __init__(self, env, table_action, tablename):
        self.env = env
        self.table_action = table_action
        self.tablename = tablename

    def on_message(self, msg):
        # decode JSON payload
        pl = msg.payload.decode("utf-8")
        logging.debug("Payload:  " + pl)
        jss = js.loads(pl)

        if self.table_action == 1:
            # INSERT SQL Statement
            self.env.dbc.insert(self.tablename, jss)

        elif self.table_action == 2:
            # UPDATE SQL Statement - NOT YET IMPLEMENTED
            # self.env.dbc.update()
            logging.critical("Update operation not implemented.")

        else:
            logging.critical("Unknown operation %d requested to on_message." % self.table_action)

        # UPDATE TableTouchCount

