from unittest import TestCase, mock, main
from connections.db import DBConnection


class TestDBConnection(TestCase):
    def test_db_connection(self):
        
        self.assertIsNone(DBConnection.instance)

        db = DBConnection(mock.MagicMock())

        assert db.conn
        assert db.cursor


if __name__ == "__main__":
    main()