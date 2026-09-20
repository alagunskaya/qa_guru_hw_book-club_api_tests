import uuid
import pytest

from helpers import register_user

BASE_URL = "https://book-club.qa.guru/api/v1"


@pytest.fixture
def unique_user():
    uid = uuid.uuid4().hex[:8]
    return {
        "username": f"testuser_{uid}",
        "password": "TestPassword",
    }


@pytest.fixture
def registered_user(unique_user):
    response = register_user(unique_user)
    assert response.status_code == 201, f"Не удалось зарегистрировать пользователя: {response.text}"
    return unique_user
