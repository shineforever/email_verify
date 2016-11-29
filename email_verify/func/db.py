import MySQLdb
import datetime
from func.assist import get_token, get_authcode


class DataBase:
    def __init__(self, hostname, user, pwd, base_name):
        self.db = MySQLdb.connect(hostname, user, pwd, base_name)
        self.cursor = self.db.cursor()
        self.base = base_name
        self.table = 'user'

    def set_table(self, table):
        self.table = table

    def query_by_id(self, id):
        sql = "select * from %s where `id`=%s" % (self.table, id)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data
        except:
            print("Error: unable to fetch data using 'id'=%s" % id)

    def query_by_email(self, name, email):
        sql = "select * from %s where name='%s' and email='%s'" % (self.table, name, email)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data
        except:
            print("Error: unable to fetch data using 'email'=%s" % email)
            return None

    def query_by_token(self, token, authcode):
        sql = "select * from %s where token='%s' and authcode='%s'" % (self.table, token, authcode)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data
        except:
            print("Error: unable to fetch data using token")
            return False

    def insert_record(self, name, email):
        id = self.get_max_id()
        if id is None:
            id = 0
        elif id == -1:
            return
        id = id + 1
        current_time = datetime.datetime.now()
        token = get_token(id, name, current_time.strftime("%Y-%m-%d %H:%M:%S"))
        authcode = get_authcode()
        sql = "insert into %s(name, email, token, authcode, created_time) values('%s', '%s', '%s', '%s', '%s')" % \
              (self.table, name, email, token, authcode, current_time)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            print('Error: unable to insert data (name:%s, email:%s)' % (name, email))
            self.db.rollback()
            return False

    def update(self, token, authcode):
        status = 1
        sql = "update %s set verification_status=%s where token='%s' and authcode='%s'" % \
              (self.table, status, token, authcode)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("commit!")
        except:
            self.db.rollback()

    def get_max_id(self):
        sql = "select max(id) from %s" % self.table
        try:
            self.cursor.execute(sql)
            id = self.cursor.fetchone()
            return id[0]
        except:
            print("Error: unable to get the last insert id")
            return -1

    def close(self):
        self.db.close()