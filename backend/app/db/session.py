from sqlmodel import create_engine, Session
from app.core.config import settings


#通用连接参数
connect_args = {}
engine_kwargs ={
    "echo":True,               #启用SQLAlchemy的日志记录功能，输出所有执行的SQL语句到控制台，方便调试和监控数据库操作
}
#
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False #SQLite特有参数，允许在不同线程中使用同一个连接，适用于多线程环境
else:
    engine_kwargs.update({
        "pool_pre_ping":True,   #关键参数：每次从连接池取连接时，先检测连接是否有效，如果无效则丢弃并创建新连接
        "pool_recycle":3600,    #关键参数：连接使用超过3600秒后自动回收，避免数据库服务器关闭长时间闲置的连接
        "pool_size":10,         #连接池的大小，指定同时可以保持的连接数量
        "max_overflow":20,      #超出pool-size的连接数后最多创建的连接数
    })

engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args,
    **engine_kwargs
)


def get_session():
    with Session(engine) as session:
        yield session
