from sqlalchemy.orm import Session

from app.models.term_model import Term

SEED_TERMS = [
    {"keyword": "API", "description": "Application Programming Interface — программный интерфейс"},
    {"keyword": "FastAPI", "description": "Современный Python-фреймворк для создания REST API"},
    {"keyword": "HTTP", "description": "Протокол передачи гипертекста, основа работы интернета"},
    {"keyword": "JSON", "description": "JavaScript Object Notation — текстовый формат обмена данными"},
    {"keyword": "ORM", "description": "Object-Relational Mapping — способ работы с базой через объекты"}
]


def seed_terms(db: Session):
    for data in SEED_TERMS:
        existing = db.query(Term).filter(Term.keyword == data["keyword"]).first()
        if not existing:
            term = Term(**data)
            db.add(term)
    db.commit()
