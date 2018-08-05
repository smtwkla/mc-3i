import json
from os import path
import pymysql.cursors
import string

def read_db_conf():
    with open(path.relpath('conf/db_config.json'), 'r') as s:
        config = json.load(s)
    return config


def filter_field_name(fn):
    valid_chars = "_%s%s" % (string.ascii_letters, string.digits)

    fn = str(fn).strip()
    ffn = ""
    for ch in fn:
        if ch in valid_chars:
            ffn += ch
    print("Filtered %s to %s" % (fn, ffn))
    return ffn


class DBConnector(object):
    """docstring for DBConnector."""

    def __init__(self):
        super(DBConnector, self).__init__()
        c = read_db_conf()
        self.db_host = c['DB']['HOST']
        self.db_port = c['DB']['PORT']
        self.db_user = c['DB']['USER']
        self.db_passwd = c['DB']['PASS']
        self.db_db = c['DB']['DB']
        self.connection = None

    def connect(self):
        print("Connecting to database " + self.db_host + ":" + str(self.db_port))
        # Connect to the database
        self.connection = pymysql.connect(host=self.db_host,
                                          user=self.db_user,
                                          password=self.db_passwd,
                                          db=self.db_db,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        return True

    def insert(self, table, record):
        # Insert New Record into table

        # Build Field, Value string
        sField = ""
        sVal = ""
        sRef = ""
        for aField in record.keys():
            field = filter_field_name(aField)    # Filter Field name of suspicious characters
            if field != aField :
                print("Field name contains illegal characters: ", aField)
                return False
            sField += "" + field + ","
            v = record[aField]
            if isinstance(v, str):
                sRef += "%(" + aField + ")s,"
            elif isinstance(v, int):
                sRef += "%(" + aField + ")s,"
            elif isinstance(v, float):
                sRef += "%(" + aField + ")s,"

        sField = sField[:-1]  # Remove the extra ,
        sRef = sRef[:-1]

        # Create a new record
        sql = "INSERT INTO " + table + " (" + sField + ") VALUES (" + sRef + ")"
        print(sql)

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, record)
                self.connection.commit()
            except (pymysql.err.InternalError,  pymysql.err.ProgrammingError) as er:
                print("Error: {0}".format(er))
                return False
            else:
                return True

    def update(self, table, record, id_field):
        # id_val = record[id_field]
        # sql = "UPDATE " + table + " SET " + sFieldVal + " WHERE " + id_field + "=" + id_val
        return True
