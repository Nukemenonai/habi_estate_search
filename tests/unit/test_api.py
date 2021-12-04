import requests
import unittest

class TestApi(unittest.TestCase):
    
    def test_get_status(self):
        expected_result = {"status": "up and running!"}

        r = requests.get("http://localhost:8000/status")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), expected_result)



if __name__ == '__main__':
    unittest.main()



