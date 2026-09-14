# Book Club API

Проект с автотестами на Python с использованием
библиотеки `requests`. Тестируется публичное API [Book Club](https://book-club.qa.guru/api/v1/docs/swagger/).

Эндпоинт `GET /api/v1/clubs/` — получение списка клубов.

Проверяется:
- доступность эндпоинта и код ответа 200;
- наличие и тип поля `results`;
- соответствие ответа JSON Schema;
- работа пагинации (`page`, `page_size`);
- работа поиска (`search`).
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