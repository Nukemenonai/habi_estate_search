from typing import Dict
import pymysql

class DBConnection:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(DBConnection)
            return cls.instance
        return cls.instance

    def __init__(self, db_name: Dict):
        self.name = db_name
        #connect takes url, dbname, user-id, password
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        try:
            return pymysql.connect(**self.name)
        except pymysql.Error as e:
            pass

    def __del__(self):
        self.cursor.close()
        self.conn.close()