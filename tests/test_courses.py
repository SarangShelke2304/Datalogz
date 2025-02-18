import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_auth_headers():
    response = client.post("/token", data={  # Correct endpoint
        "username": "user",
        "password": "password"
    })
    assert response.status_code == 200, f"Auth failed: {response.json()}"
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}



def test_create_course():
    headers = get_auth_headers()

    response = client.post("/courses/", json={
        "title": "Math",
        "description": "Algebra 101"
    }, headers=headers)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Math"


if __name__ == "__main__":
    pytest.main()
