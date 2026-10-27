import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    payload = response.get_json()
    assert payload['service'] == 'gitops-platform-demo'
    assert payload['status'] == 'healthy'


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    payload = response.get_json()
    assert payload['status'] == 'ok'


def test_metrics(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'gitops_app_requests_total' in response.data
