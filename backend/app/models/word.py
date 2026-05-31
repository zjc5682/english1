from typing import Optional #导入Optional类型提示，表示某个字段可以是指定类型或None
from sqlmodel import SQLModel, Field #导入SQLModel基类和Field函数，用于定义数据库模型

class Word(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    english:str = Field(index = True)
    chinese:str
    part_of_speech:str
    example_sentence:str
    part_of_speech:Optional[str] =None
    example_sentence:Optional[str]=None
    difficulty:int = Field(default = 1)