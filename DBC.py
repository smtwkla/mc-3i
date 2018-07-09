import json
import  pymysql.cursors

def read_db_conf():
    with open('db_config.json', 'r') as s:
        config = json.load(s)
    return config


class DBConnector(object):
    """docstring for DBConnector."""
    def __init__(self):
        super(DBConnector, self).__init__()
        c=read_db_conf()
        self.db_host= c['DB']['HOST']
        self.db_port= c['DB']['PORT']
        self.db_user= c['DB']['USER']
        self.db_passwd= c['DB']['PASS']
        self.db_db= c['DB']['DB']

    def connect(self):
        print "Connecting to database " + self.db_host + ":" + str(self.db_port)
        # Connect to the database
        self.connection = pymysql.connect(host=self.db_host,
                                     user=self.db_user,
                                     password=self.db_passwd,
                                     db=self.db_db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return True

    def insert(self):
        return True

    def update(self):
        return True
