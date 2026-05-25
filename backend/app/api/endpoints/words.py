from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.word import Word
from app.schemas.word import WordCreate, WordRead

router = APIRouter(prefix="/words", tags=["words"])

@router.post("/", response_model=WordRead)
def create_word(word: WordCreate, session: Session = Depends(get_session)):
    db_word = Word.model_validate(word)
    session.add(db_word)
    session.commit()
    session.refresh(db_word)
    return db_word

@router.get("/", response_model=list[WordRead])
def read_words(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    words = session.exec(select(Word).offset(skip).limit(limit)).all()
    return words
