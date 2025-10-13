from app.core.database import SessionLocal
from app.core.seed import seed_terms

db = SessionLocal()
try:
    seed_terms(db)
    print("Термины успешно добавлены!")
finally:
    db.close()
