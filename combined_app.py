

import requests
import json
import csv
import pytest

# ----------------- APP FUNCTIONS -----------------

def fetch_users(url):
    """Fetch data from API with error handling"""
    try:
        response = requests.get(url, timeout=5)
        return response
    except requests.RequestException as e:
        raise RuntimeError(f"API error: {e}")

def is_valid_user(user):
    """Check if user has mandatory fields"""
    return all(field in user and user[field] for field in ("id", "name", "email"))

def validate_response(response):
    """Validate API response"""
    if response.status_code != 200:
        raise ValueError("Invalid status code")
    if "application/json" not in response.headers.get("Content-Type", ""):
        raise ValueError("Invalid content type")
    data = response.json()
    if not isinstance(data, list):
        raise ValueError("Invalid JSON structure")
    return [u for u in data if is_valid_user(u)]

def save_to_json(filename, data):
    """Save valid data to JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_to_csv(filename, data):
    """Save valid data to CSV file (only id, name, email)"""
    fieldnames = ["id", "name", "email"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({k: row[k] for k in fieldnames})

# ----------------- MAIN APP -----------------

URL = "https://jsonplaceholder.typicode.com/users"

def run_app():
    response = fetch_users(URL)
    users = validate_response(response)
    print(f"API request successful: {response.status_code} OK")
    print(f"Valid records processed: {len(users)}")
    save_to_json("users.json", users)
    save_to_csv("users.csv", users)
    print("Data saved to users.json")
    print("Data saved to users.csv")

# ----------------- PYTEST TESTS -----------------

@pytest.fixture
def valid_api_data():
    return [
        {"id": 1, "name": "Alice", "email": "a@test.com"},
        {"id": 2, "name": "Bob", "email": "b@test.com"},
        {"id": 3, "name": "", "email": "c@test.com"}  # invalid
    ]

class FakeResponse:
    def __init__(self, status, data, content_type="application/json"):
        self.status_code = status
        self._data = data
        self.headers = {"Content-Type": content_type}
    def json(self):
        return self._data

@pytest.mark.parametrize("status,data,expected", [
    (200, [{"id":1,"name":"A","email":"a@test.com"}], 1),
    (200, [{"id":1,"name":"","email":"a@test.com"}], 0)
])
def test_api_success(status, data, expected):
    response = FakeResponse(status, data)
    result = validate_response(response)
    assert len(result) == expected

def test_api_invalid_response():
    response = FakeResponse(404, [])
    with pytest.raises(ValueError):
        validate_response(response)

def test_file_write(valid_api_data, tmp_path):
    file_json = tmp_path / "test.json"
    file_csv = tmp_path / "test.csv"
    save_to_json(file_json, valid_api_data)
    save_to_csv(file_csv, valid_api_data)
    assert file_json.exists()
    assert file_csv.exists()

def test_invalid_content_type():
    response = FakeResponse(200, [], "text/html")
    with pytest.raises(ValueError):
        validate_response(response)

@pytest.mark.xfail(reason="Future enhancement")
def test_future_feature():
    assert False

# ----------------- RUN APP OR TESTS -----------------
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        pytest.main([__file__, "-v"])
    else:
        run_app()
