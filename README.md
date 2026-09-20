# Book Club API

Проект с автотестами на Python с использованием
библиотеки `requests`. Тестируется публичное API [Book Club](https://book-club.qa.guru/api/v1/docs/swagger/).

## Тесты

| Файл | Что покрывает                                      |
|------|----------------------------------------------------|
| `test_register.py` | Регистрация пользователя                           |
| `test_auth.py` | Авторизация (JWT)                                  |
| `test_clubs.py` | Список клубов, пагинация, поиск                    |
| `test_club_crud.py` | CRUD клуба (создание, чтение, обновление, удаление) |
## Установка
```bash
# клонировать репозиторий
git clone <ссылка-на-репозиторий>
cd <папка-проекта>

# создать и активировать виртуальное окружение
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows

# установить зависимости
pip install -r requirements.txt
```
## Запуск тестов
```bash
# все тесты
pytest test_clubs.py -v

# с выводом print в консоль
pytest test_clubs.py -v -s

# только один тест
pytest test_clubs.py::test_search_clubs -v
```