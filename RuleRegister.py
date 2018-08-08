

class RuleRegisterClass:

    def __init__(self, env):
        self.env = env
        self.rules = []

    def load_rules_table(self):
        pass

    def reload_rules_table(self):
        pass

    def add_rule(self, rule):
        self.rules.append(rule)

    def remove_rule(self, rule):
        if rule in self.rules:
            self.rules.remove(rule)

    def modify_rule(self):
        pass

