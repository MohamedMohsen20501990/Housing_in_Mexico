from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"area": 60, "lat": 19.9, "lon": -99.8})
    assert response.status_code ==200
    assert response.json()["success"] == True
    assert "prediction" in response.json().keys()
    
    