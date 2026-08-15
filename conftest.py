import pytest
import requests
from config import settings

@pytest.fixture(scope="session")
def api_session():
    """Session fixture for API requests."""
    session = requests.Session()
    session.headers.update(settings.DEFAULT_HEADERS)
    session.timeout = settings.API_TIMEOUT
    return session

@pytest.fixture(scope="session")
def base_url():
    return settings.BASE_URL
