from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.term_model import Term
from app.schemas.term import TermResponse, TermCreate, TermUpdate

router = APIRouter()


@router.get("/glossary", response_model=list[TermResponse], tags=["Glossary"])
def get_terms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Term).offset(skip).limit(limit).all()


@router.get("/glossary/{keyword}", response_model=TermResponse, tags=["Glossary"])
def get_term(keyword: str, db: Session = Depends(get_db)):
    term = db.query(Term).filter(Term.keyword == keyword).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    return term


@router.post("/glossary", response_model=TermResponse, status_code=201, tags=["Glossary"])
def create_term(term: TermCreate, db: Session = Depends(get_db)):
    existing = db.query(Term).filter(Term.keyword == term.keyword).first()
    if existing:
        raise HTTPException(status_code=400, detail="Term already exists")
    db_term = Term(keyword=term.keyword, description=term.description)
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term


@router.put("/glossary/{keyword}", response_model=TermResponse, tags=["Glossary"])
def update_term(keyword: str, update: TermUpdate, db: Session = Depends(get_db)):
    term = db.query(Term).filter(Term.keyword == keyword).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    term.description = update.description
    db.commit()
    db.refresh(term)
    return term


@router.delete("/glossary/{keyword}", status_code=204, tags=["Glossary"])
def delete_term(keyword: str, db: Session = Depends(get_db)):
    term = db.query(Term).filter(Term.keyword == keyword).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    db.delete(term)
    db.commit()
