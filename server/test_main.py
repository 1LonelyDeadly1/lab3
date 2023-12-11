from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_predict():
    response = client.post("/api/model", params={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json()["target_name"] == '__label__eng_Latn'
