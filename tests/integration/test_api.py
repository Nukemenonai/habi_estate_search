import json
import pytest
import requests


@pytest.mark.integration
def test_api_status():
    expected_result = {
        'APP_NAME': 'Estate Search',
        'VERSION': '1.0.0',
        'status': 'up and running!'
    }
    r = requests.get("http://localhost:8000/status")
    assert r.status_code == 200
    assert r.json() == expected_result
 
@pytest.mark.integration
def test_api_estate():
    data = {
    "city": "bogota",
    "statuses": [3, 4],
    "year": 2000
    }
    r = requests.post("http://localhost:8000/estate", json=json.dumps(data))
    assert r.status_code == 200
