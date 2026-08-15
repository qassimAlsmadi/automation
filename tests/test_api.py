import pytest
from config import settings

@pytest.mark.api
def test_get_post(api_session, base_url):
    """Test retrieving a specific post."""
    response = api_session.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    print(f"✅ Test passed! Title: {data['title']}")

@pytest.mark.api
def test_create_post(api_session, base_url):
    """Test creating a new post."""
    payload = {"title": "Automation Test", "body": "Body text", "userId": 1}
    response = api_session.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Automation Test"
    print("✅ Create post test passed!")
