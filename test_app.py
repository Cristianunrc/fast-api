from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Wellcome": "Wellcome to my REST API"}

def test_create_post():
    response = client.post(
        "/posts",
        json={
            "id": "1",
            "title": "Test Post",
            "author": "Jhon Doe",
            "content": "This is a test post",
        }
    )

    response_json = response.json()

    assert response.status_code == 200
    assert response_json["title"] == "Test Post"
    assert response_json["author"] == "Jhon Doe"
    assert response_json["content"] == "This is a test post"
