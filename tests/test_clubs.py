import requests
from jsonschema import validate

from schemas.schema import CLUBS_LIST_SCHEMA

BASE_URL = "https://book-club.qa.guru/api/v1/clubs/"


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


def test_get_clubs_real_content():
    response = requests.get(BASE_URL)
    first_club = response.json()["results"][0]

    assert len(first_club["bookTitle"].strip()) >= 3
    assert len(first_club["bookAuthors"].strip()) >= 3
    assert isinstance(first_club["publicationYear"], int)


def test_get_clubs_page_size():
    # page_size ограничивает количество элементов
    response = requests.get(BASE_URL, params={"page": 1, "page_size": 2})
    data = response.json()

    assert response.status_code == 200
    assert len(data["results"]) == 2


def test_search_clubs():
    first_club = requests.get(BASE_URL).json()["results"][0]
    search_item = first_club["bookTitle"]

    response = requests.get(BASE_URL, params={"search": search_item})
    data = response.json()

    assert response.status_code == 200
    assert data["count"] >= 1
    assert search_item in data["results"][0]["bookTitle"]
