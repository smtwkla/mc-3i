import logging
import Actions
import Rule as RuleClass


class RuleRegisterClass:

    def __init__(self, env):
        self.env = env
        self.rules = []

    def load_rules_table(self):

        sql_fld = "RuleName, RuleID, Topic, Operation, TableName, last_modified"
        sql_where = "3i_Rules.Enabled = TRUE"
        res = self.env.dbc.select("3i_Rules", sql_fld, condition=sql_where, group_by=None, limit="10000")
        rule_res = res.fetchall()

        # Parse Direct Table Write Action Topics to be subscribed to from JSON File and add it to RuleList[]
        for aTopic in rule_res:
            logging.debug(aTopic)
            if aTopic['Operation'] in (1, 2):
                w = Actions.WriteTableActionClass(self.env, aTopic['Operation'], aTopic['TableName'])
                r = RuleClass.Rule(name=aTopic['RuleName'], topic=aTopic['Topic'], rule_action=w,
                                   time_stamp=['last_modified'])
                self.env.rr.add_rule(r)
            else:
                erm = "Error: Unimplemented Action Rule Operation %s for rule %s" % (aTopic['Operation'], aTopic['RuleName'])
                logging.critical(erm)
                self.env.quit_err()

    def reload_rules_table(self):
        pass

    def add_rule(self, rule):
        self.rules.append(rule)

    def remove_rule(self, rule):
        if rule in self.rules:
            self.rules.remove(rule)

    def modify_rule(self):
        pass

