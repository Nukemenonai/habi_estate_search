"""General settings"""

import os

MYSQL_HOST = os.getenv("SQL_HOST")
MYSQL_PORT = os.getenv("SQL_PORT")
MYSQL_USER = os.getenv("SQL_USER")
MYSQL_PASSWORD = os.getenv("SQL_PASSWORD")
MYSQL_DB = os.getenv("SQL_DATABASE")

APP_NAME = "Estate Search"
CONN_NAME = {
    "host": MYSQL_HOST,
    "port": MYSQL_PORT,
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "database": MYSQL_DB,
}
VERSION = "1.0.0"
