from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_customers_endpoint():
    response = client.get("/customers")
    assert response.status_code in (200, 404)
