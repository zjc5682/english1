from datetime import datetime,timezone #导入datetime模块中的datetime和timezone类，用于处理日期和时间
from typing import Optional,TYPE_CHECKING #导入typing模块中的Optional类型，用于表示可选的参数类型
from sqlmodel import SQLModel, Field,Relationship,UniqueConstraint #导入sqlmodel模块中的SQLModel基类和Field函数，用于定义数据库模型


if TYPE_CHECKING: #TYPE_CHECKING是一个特殊的常量，在类型检查时为True，在运行时为False，用于避免循环导入问题
    from app.models.word import Word
    from app.models.user import User
#default=None表示该字段在数据库中默认为空值，
    # primary_key=True表示该字段是主键，foreign_key参数指定了外键关系，
    # index=True表示为该字段创建索引以提高查询性能
class UserWordProgress(SQLModel, table =True):
    __table_args__=(UniqueConstraint("user_id","word_id",name="uix_user_word")) #添加唯一约束，确保同一用户对同一单词的进度记录唯一
    
    id: Optional[int] = Field(default=None,primary_key=True)
    user_id:int = Field(foreign_key="user.id",index=True)
    word_id:int = Field(foreign_key="word.id",index=True)

   
    
    #掌握程度：0=未学，
    level:int = Field(default=0)

    #下次复习时间
    next_review:Optional[datetime] = Field(default=None)

    #统计数据
    correct_count:int = Field(default=0)
    incorrect_count:int = Field(default=0)
    last_studied:Optional[datetime] = Field(default=None)

    #可选：记录学习次数
    study_count:int = Field(default = 0) 
    #Field函数用于定义数据库模型的字段，设置默认值为0

    #创建和更新时间
    create_at:datetime = Field(default_factory=lambda:datetime.now(timezone.utc))
    update_at:datetime = Field(default_factory=lambda:datetime.now(timezone.utc))
    #datetime.now(timezone.utc)获取当前的UTC时间，作为默认值，确保时间记录的一致性和时区无关性
    #Field函数的default_factory参数接受一个函数，当创建新记录时会调用该函数来生成默认值，
    #这里使用lambda表达式来调用datetime.now(timezone.utc)获取当前时间
    
    user: "User" = Relationship(back_populates="progresses")
    word: "Word" = Relationship()
    #Relationship函数用于定义模型之间的关系，back_populates参数指定了反向关系的属性名称，






