import json
from os import path
import pymysql.cursors
import string
import logging

def read_db_conf(conf):
    with open(path.relpath(conf + '/db_config.json'), 'r') as s:
        config = json.load(s)       # Read JSON String from config file
    return config


def filter_field_name(fn):
    # Strip illegal characters from passed string
    valid_chars = "_%s%s" % (string.ascii_letters, string.digits)

    fn = str(fn).strip()    # Strip extra spaces
    ffn = ""

    for ch in fn:
        if ch in valid_chars:
            ffn += ch

    # print("Filtered %s to %s" % (fn, ffn)) # Debug output

    return ffn


class DBConnector(object):
    """docstring for DBConnector."""

    def __init__(self, conf):
        super(DBConnector, self).__init__()
        c = read_db_conf(conf)
        self.db_host = c['DB']['HOST']
        self.db_port = c['DB']['PORT']
        self.db_user = c['DB']['USER']
        self.db_passwd = c['DB']['PASS']
        self.db_db = c['DB']['DB']
        self.connection = None

    def connect(self):
        logging.info("Connecting to database " + self.db_host + ":" + str(self.db_port))
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

        self.ping()

        # Build Field, Value string
        sField = ""
        sVal = ""
        sRef = ""
        for aField in record.keys():

            field = filter_field_name(aField)  # Filter Field name of suspicious characters

            if field != aField or field == "":
                # Field name in record contains illegal characters.
                logging.error("Field name contains illegal characters %s or is empty." % aField)
                return False    # Terminate action

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
        logging.debug(sql)  # Debug output

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, record)
                self.connection.commit()

            except (pymysql.err.InternalError, pymysql.err.ProgrammingError) as er:
                logging.error("Error: {0}".format(er))
                return False

            else:
                return True

    def update(self, table, record, condition):

        self.ping()

        sField = ""

        for aField in record.keys():
            field = filter_field_name(aField)  # Filter Field name of suspicious characters

            if field != aField or field == "":
                # Field name in record contains illegal characters.
                logging.error("Field name contains illegal characters %s or is empty." % aField)
                return False  # Terminate action

            sField += "" + field + "="
            v = record[aField]

            if isinstance(v, str):
                sField += "%(" + aField + ")s,"
            elif isinstance(v, int):
                sField += "%(" + aField + ")s,"
            elif isinstance(v, float):
                sField += "%(" + aField + ")s,"

        sField = sField[:-1]  # Remove the extra ,
        sql = "UPDATE " + table + " SET " + sField + " WHERE " + condition
        logging.debug(sql)

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql, record)
                self.connection.commit()

            except pymysql.err.Error as er:
                logging.error("Error: {0}".format(er))
                return False

            else:
                return True

    def delete(self, table, condition):

        self.ping()

        sql = "DELETE FROM " + table + " WHERE " + condition
        logging.debug(sql)

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.connection.commit()

            except pymysql.err.Error as er:
                logging.error("Error: {0}".format(er))
                return False

            else:
                return True

    def select(self, table, fields, condition=None, order_by=None, group_by=None, limit=None):

        self.ping()

        sql = "SELECT " + fields + " FROM " + table
        if condition is not None:
            sql += " WHERE " + condition
        if order_by is not None:
            sql += " ORDER BY " + order_by
        if group_by is not None:
            sql += " GROUP BY " + group_by
        if limit is not None:
            sql += " LIMIT " + limit

        logging.debug(sql)

        cursor = self.connection.cursor()
        try:
            cursor.execute(sql)
            return cursor
        except pymysql.err.Error as er:
            logging.error("Error: {0}".format(er))
            return None

    def ping(self, recon):
        if __name__ == '__main__':
            self.connection.ping(recon)
