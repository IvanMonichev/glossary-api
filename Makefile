.PHONY: run seed

run:
	uvicorn app.main:app --reload

seed:
	python seed_db.py
