import Actions
import json as js


class WriteTableActionClass(Actions.RuleActionClass):

    def __init__(self, env, insert, tablename):
        self.env = env
        self.insert = insert
        self.tablename = tablename

    def on_message(self, msg):
        # decode JSON payload
        pl = msg.payload.decode("utf-8")
        print("Payload:  ")
        print(pl)
        jss = js.loads(pl)
        print(jss)

        if self.insert:
            # INSERT SQL Statement
            self.env.dbc.insert(self.tablename, jss)

        else:
            # UPDATE SQL Statement
            self.env.dbc.update()
        # UPDATE TableTouchCount

