from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_add():
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json["result"] == 5

def test_multiply():
    response = client.get("/multiply?a=4&b=5")
    assert response.status_code == 200
    assert response.json["result"] == 20