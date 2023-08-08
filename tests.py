import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert b'Calculator App' in response.data

def test_calculate_valid_input(client):
    data = {
        'num1': 5,
        'num2': 3,
        'operator': 'add'
    }
    response = client.post('/calculate', json=data)
    assert response.status_code == 200
    expected_response = {'result': 8}
    response_data = json.loads(response.data.decode('utf-8'))
    assert response_data == expected_response

def test_calculate_invalid_input(client):
    data = {
        'num1': 'abc',
        'num2': 3,
        'operator': 'add'
    }
    response = client.post('/calculate', json=data)
    assert response.status_code == 400
    expected_error = {'error': 'Invalid input'}
    response_data = json.loads(response.data.decode('utf-8'))
    assert response_data == expected_error

def test_calculate_divide_by_zero(client):
    data = {
        'num1': 10,
        'num2': 0,
        'operator': 'divide'
    }
    response = client.post('/calculate', json=data)
    assert response.status_code == 400
    expected_error = {'error': 'Cannot divide by zero'}
    response_data = json.loads(response.data.decode('utf-8'))
    assert response_data == expected_error

def test_calculate_invalid_operator(client):
    data = {
        'num1': 5,
        'num2': 3,
        'operator': 'invalid'
    }
    response = client.post('/calculate', json=data)
    assert response.status_code == 400

    response_data = json.loads(response.data.decode('utf-8'))
    expected_error_message = 'Invalid operator'
    assert 'error' in response_data
    assert response_data['error'] == expected_error_message
