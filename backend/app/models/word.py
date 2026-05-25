from typing import Optional
from sqlmodel import SQLModel, Field

class Word(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    english: str = Field(index=True)
    chinese: str
    part_of_speech: Optional[str] = None
    example_sentence: Optional[str] = None
