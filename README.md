# 🧠 FastAPI Glossary

**REST API-сервис глоссария терминов**, реализованный с использованием **FastAPI**, **SQLAlchemy**, **Pydantic** и **Alembic**.  
Проект позволяет управлять коллекцией терминов (создавать, просматривать, редактировать и удалять).

Документация автоматически формируется на основе OpenAPI-спецификации и доступна в интерфейсе Swagger.

## Установка и запуск
```bash
python -m venv venv
source venv/bin/activate  # для Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск сервера
```bash
uvicorn app.main:app --reload
```

## Настройка окружения
Создайте файл .env в корне проекта, можно скопировать `env-example`.

## Makefile
```makefile
run:        # запуск API
	uvicorn app.main:app --reload

seed:       # сидирование базы
	python seed_db.py

db:         # удаление и пересоздание базы
	rm -f database/glossary.db && python seed_db.py
```