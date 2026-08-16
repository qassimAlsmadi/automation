import json
import os

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def get_test_data(filename):
    """Get test data from fixtures folder."""
    base_path = os.path.join(os.path.dirname(__file__), '..', 'fixtures')
    return load_json(os.path.join(base_path, filename))
