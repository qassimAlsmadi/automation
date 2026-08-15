import os
# Base URLs
BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
TARGET_WEB_URL = os.getenv("TARGET_WEB_URL", "http://localhost:3000")
# Timeouts
API_TIMEOUT = 10
WEB_TIMEOUT = 30
# Headers
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
