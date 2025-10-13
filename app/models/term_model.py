from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base


class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Term(id={self.id}, keyword='{self.keyword}')>"
