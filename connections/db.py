"""Database connection class"""

from typing import Dict
import pymysql
import logging


class DBConnection:
    """Class that controls the connection to the database. 
    """
    instance = None

    def __new__(cls, *args, **kwargs):
        """Return a new instance of class if there is none.

        Returns
        -------
        DBConnection
            Object of the DBBConnection class
        """
        if cls.instance is None:
            cls.instance = super().__new__(DBConnection)
            return cls.instance
        return cls.instance

    def __init__(self, db_name: Dict):
        """Initialize a class instance

        Parameters
        ----------
        db_name : Dict
            Dictionary containing all arguments for database connection
        """
        self.name = db_name
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        """Return a connection to a database

        Returns
        -------
        Connection
            Connection object as specified by python database API reference
        """
        try:
            return pymysql.connect(**self.name)
        except pymysql.Error as e:
            logging.error(f"{e}")

    def query(self, sql_query: str):
        """Perform a query and return the result

        Parameters
        ----------
        sql_query : str
            String that contains a SQL query

        Returns
        -------
        tuple
            Query results expressed as a tuple. 
        """
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def __del__(self):
        """Destroy the current connection instance. 
        """
        self.cursor.close()
        self.conn.close()
