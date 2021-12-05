import requests
import unittest
import json

class TestApi(unittest.TestCase):
    
    def test_get_status(self):
        expected_result = {"status": "up and running!"}

        r = requests.get("http://localhost:8000/status")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), expected_result)
        data = {'some': 'value'}
        expected_result = {"posted": "ok"}
        r = requests.post("http://localhost:8000/estate", json=json.dumps(data))
        self.assertEqual(r.status_code, 200)
        #self.assertEqual(expected_result, r.json())



if __name__ == '__main__':
    unittest.main()



