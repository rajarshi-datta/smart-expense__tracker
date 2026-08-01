from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        },
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Lunch"
    assert data["amount"] == 250
    assert data["category"] == "Food"


def test_filter_by_category():
    response = client.get("/expenses/category/Food")

    assert response.status_code == 200


def test_total_expenses():
    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert "total" in response.json()


def test_delete_expense():
    response = client.delete("/expenses/1")

    assert response.status_code in [200, 404]