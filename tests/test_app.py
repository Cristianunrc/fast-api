from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def create_post():
    post_data = {
        "title": "Test Post",
        "author": "Jhon Doe",
        "content": "This is a test post",
    }
    reponse = client.post("/posts", json=post_data)
    return reponse

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Wellcome": "Wellcome to my REST API"}

def test_create_post():
    response = create_post()
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["title"] == "Test Post"
    assert response_json["author"] == "Jhon Doe"
    assert response_json["content"] == "This is a test post"

def test_negative_get_post():
    response = client.get('/posts/1')
    assert response.status_code == 404
    assert response.json() == {"detail": "Post Not found"}

def test_get_post():
    response = create_post()
    response_json = response.json()
    post_id = response_json["id"]
    response_one = client.get(f'/posts/{post_id}')
    assert response_one.status_code == 200
    assert response_json == response_one.json()

def test_negative_delete_post():
    response = client.post('/posts/1')
    assert response.status_code == 404
    assert response.json() == {"detail": "Post Not found"}

def test_delete_post():
    response = create_post()
    response_json = response.json()
    post_id = response_json["id"]
    response_delete = client.post(f'/posts/{post_id}')
    assert response_delete.status_code == 200
    assert response_delete.json() == {"message": "Successfully deleted"}

def test_negative_update_post():
    response = client.put(
        '/posts/1',
        json={
            "id": "1",
            "content": "This is an updated test post",
        }
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Post Not found"}

def test_update_post():
    response = create_post()
    response_json = response.json()
    response_json["content"] = "This is an updated test post"
    post_id = response_json["id"]
    response_update = client.put(
        f'/posts/{post_id}',
        json=response_json
    )
    assert response_update.status_code == 200
    assert response_update.json() == {"message": "Successfully updated"}
