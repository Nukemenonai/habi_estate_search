"""General settings"""

import os

MYSQL_HOST = os.getenv("MYSQL_HOST", "3.130.126.210")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3309))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB", "habi_db")

APP_NAME = "Estate Search"
CONN_NAME = {
    "host": MYSQL_HOST,
    "port": MYSQL_PORT,
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "database": MYSQL_DB,
}
VERSION = "1.0.0"
