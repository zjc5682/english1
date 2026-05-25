from typing import Optional
from pydantic import BaseModel

class WordCreate(BaseModel):
    english: str
    chinese: str
    part_of_speech: Optional[str] = None
    example_sentence: Optional[str] = None

class WordRead(WordCreate):
    id: int

    class Config:
        from_attributes = True
