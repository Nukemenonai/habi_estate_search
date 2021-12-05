from connections.db import DBConnection


def test_db_connection():
    name = {"host": "3.130.126.210", "port": 3309, "user": "pruebas", "password":"VGbt3Day5R", "database": "habi_db"}
    db = DBConnection(name)
    assert db.conn.open


if __name__ == "__main__":
    test_db_connection()