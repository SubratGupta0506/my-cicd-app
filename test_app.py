from app import app

def test_home():
    # Create a test version of the app
    client = app.test_client()
    
    # Send a request to the home page
    response = client.get("/")
    
    # Check that it returns status 200 (means OK!)
    assert response.status_code == 200
    
    # Check that our message is in the response
    assert b"Hello" in response.data