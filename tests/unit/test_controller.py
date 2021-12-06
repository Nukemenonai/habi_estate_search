import requests
import json
from unittest import TestCase, mock, main
from controllers.get_estate import GetEstateController



class TestController(TestCase):

    def test_get_estate(self):
        mockdb = mock.MagicMock()
        mockdb.query = mock.MagicMock()
        request_params = {
            "city": "bogota",
            "statuses": [3, 4],
            "year": 2000
        }

        response = GetEstateController.get_estate(
            db=mockdb,
            request_params=request_params
        )

        self.assertTrue(mockdb.query.called)

if __name__ == "__main__":
    main()
