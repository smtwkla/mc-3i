import json

def read_db_conf():
    with open('db_config.json', 'r') as s:
        config = json.load(s)
    return config


class DBConnector(object):
    """docstring for DBConnector."""
    def __init__(self):
        super(DBConnector, self).__init__()
        c=read_db_conf()
        print c['DB']['HOST']
        print c['DB']['PORT']

    def connect(self):        
        return True

    def insert(self):
        return True

    def update(self):
        return True
