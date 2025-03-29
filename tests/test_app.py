# filepath: /Users/johnnycheng/projects/python_ms/tests/test_app.py
import sys
import os
import json

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'hello Johnny'

def test_health_endpoint(client):
    response = client.get('/health')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['status'] == 'healthy'