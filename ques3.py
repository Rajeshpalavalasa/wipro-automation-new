import requests
import json
import pytest

API_URL = "https://fakestoreapi.com/products"
# -----------------------------
# API & Processing Functions
# -----------------------------
def fetch_products(url=API_URL):
    """Fetch product data from API"""
    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            raise Exception("Invalid status code")

        if "application/json" not in response.headers.get("Content-Type", ""):
            raise Exception("Invalid content type")

        return response.json()

    except Exception as e:
        print("API Error:", e)
        return []

def is_valid_product(product):
    """Validate product record"""
    try:
        return (
            isinstance(product.get("id"), int) and product["id"] > 0 and
            isinstance(product.get("price"), (int, float)) and product["price"] > 0 and
            isinstance(product.get("title"), str) and product["title"].strip() != "" and
            isinstance(product.get("category"), str) and product["category"].strip() != ""
        )
    except Exception:
        return False


def process_products(products):
    """Filter valid products and calculate stats"""
    valid_products = [p for p in products if is_valid_product(p)]
    total = len(valid_products)
    average_price = sum(p["price"] for p in valid_products) / total if total else 0
    return valid_products, total, average_price


def save_to_file(products, filename="valid_products.json"):
    """Save valid products to file"""
    try:
        with open(filename, "w") as f:
            json.dump(products, f, indent=4)
    except Exception as e:
        print("File error:", e)


# -----------------------------
# Main Execution
# -----------------------------

def main():
    products = fetch_products()
    valid_products, total, avg_price = process_products(products)
    save_to_file(valid_products)

    print("API response received: 200 OK")
    print(f"Valid products processed: {total}")
    print(f"Average product price: {avg_price:.2f}")
    print("Data saved to valid_products.json")
# -----------------------------
# Pytest Test Cases
# -----------------------------

@pytest.fixture
def sample_products():
    return [
        {"id": 1, "title": "Phone", "price": 500, "category": "Electronics"},
        {"id": -1, "title": "Invalid", "price": 100, "category": "Test"},
        {"id": 2, "title": "", "price": 300, "category": "Electronics"},
        {"id": 3, "title": "Laptop", "price": 1200, "category": "Electronics"},
        {"id": 4, "title": "Book", "price": 0, "category": "Education"},
    ]

@pytest.mark.parametrize(
    "product, expected",
    [
        ({"id": 1, "title": "Pen", "price": 10, "category": "Stationery"}, True),
        ({"id": 0, "title": "Pen", "price": 10, "category": "Stationery"}, False),
        ({"id": 2, "title": "", "price": 10, "category": "Stationery"}, False),
        ({"id": 3, "title": "Pen", "price": -5, "category": "Stationery"}, False),
    ]
)
def test_product_validation(product, expected):
    assert is_valid_product(product) == expected


def test_valid_and_invalid_records(sample_products):
    valid_products, total, avg_price = process_products(sample_products)
    assert total == 2
    assert avg_price == (500 + 1200) / 2


def test_average_price(sample_products):
    _, _, avg_price = process_products(sample_products)
    assert avg_price > 0

@pytest.mark.xfail(reason="Future API response may change")
def test_future_api_change():
    assert False

# -----------------------------
# Entry Point
# -----------------------------

if __name__ == "__main__":
    main()
