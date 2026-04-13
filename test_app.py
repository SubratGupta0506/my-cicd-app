import pytest
from app import app

# ─────────────────────────────────────
# SETUP - runs before each test
# ─────────────────────────────────────
@pytest.fixture
def client():
    """Create a test version of our app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ─────────────────────────────────────
# TEST 1: Does home page load?
# ─────────────────────────────────────
def test_home_page_loads(client):
    """Test that home page returns 200 OK"""
    response = client.get("/")
    
    assert response.status_code == 200, \
        f"Expected 200 but got {response.status_code}"
    
    print("✅ Home page loads successfully!")

# ─────────────────────────────────────
# TEST 2: Does home page show right message?
# ─────────────────────────────────────
def test_home_page_content(client):
    """Test that home page shows correct message"""
    response = client.get("/")
    
    assert b"Hello" in response.data, \
        "Expected 'Hello' in response"
    
    print("✅ Home page shows correct content!")

# ─────────────────────────────────────
# TEST 3: Does wrong URL give 404?
# ─────────────────────────────────────
def test_wrong_url_gives_404(client):
    """Test that unknown pages return 404"""
    response = client.get("/this-page-does-not-exist")
    
    assert response.status_code == 404, \
        f"Expected 404 but got {response.status_code}"
    
    print("✅ Wrong URL correctly returns 404!")