import requests
from jsonschema import validate

from schemas.schema import CLUBS_LIST_SCHEMA

BASE_URL = "https://book-club.qa.guru/api/v1/clubs/"


def test_get_clubs_status_200():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_get_clubs_has_results():
    # в ответе есть список клубов
    response = requests.get(BASE_URL)
    data = response.json()

    assert "results" in data
    assert isinstance(data["results"], list)
    assert data["count"] >= 0


def test_get_clubs_matches_schema():
    # ответ соответствует JSON-схеме - "modified": {"type": ["string", "null"]}
    response = requests.get(BASE_URL)
    data = response.json()

    validate(instance=data, schema=CLUBS_LIST_SCHEMA)


def test_get_clubs_page_size():
    # page_size ограничивает количество элементов
    response = requests.get(BASE_URL, params={"page": 1, "page_size": 2})
    data = response.json()

    assert response.status_code == 200
    assert len(data["results"]) <= 2


def test_search_clubs():
    # поиск первого клуба
    first_club = requests.get(BASE_URL).json()["results"][0]
    search_item = first_club["bookTitle"]
    print(f"\n{search_item}")

    response = requests.get(BASE_URL, params={"search": search_item})
    data = response.json()
    print(response.url)

    assert response.status_code == 200
    assert data["count"] >= 1
