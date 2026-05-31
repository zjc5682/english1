from typing import TYPE_CHECKING,Optional,TYPE_CHECKING
from sqlmodel import SQLModel, Field,Relationship

if TYPE_CHECKING:
    from app.models.progress import UserWordProgress
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)

    progresses:list["UserWordProgress"] = Relationship(back_populates="user")

