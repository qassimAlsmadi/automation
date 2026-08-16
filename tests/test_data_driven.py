import pytest
from utils.helpers import get_test_data

@pytest.mark.api
def test_get_post_by_id(api_session, base_url):
    """Test retrieving posts using data from JSON file."""
    posts = get_test_data('test_posts.json')
    for post in posts:
        response = api_session.get(f"{base_url}/posts/{post['id']}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == post["id"]
        assert data["title"] == post["title"]
        print(f"✅ Post {post['id']} verified: {post['title']}")
