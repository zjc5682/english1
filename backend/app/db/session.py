from sqlmodel import create_engine, Session
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL, 
    echo=True,
    pool_pre_ping=True,         #关键参数：每次从连接池取连接时，先检测连接是否有效，如果无效则丢弃并创建新连接
    pool_recycle=3600,       #关键参数：连接使用超过3600秒后自动回收，避免数据库服务器关闭长时间闲置的连接
    pool_size=10,               #连接池的大小，指定同时可以保持的连接数量
    max_overflow=20,            #超出pool-size的连接数后最多创建的连接数
    )


def get_session():
    with Session(engine) as session:
        yield session
