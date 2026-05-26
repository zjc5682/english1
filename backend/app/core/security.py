from datetime import datetime,timedelta
from typing import Optional

from jose import JWTError,jwt
from passlib.context import CryptContext
from app.core.config import settings

#作用：初始化密码哈希处理器，[bcrypt]是使用的哈希算法，deprecated="auto"自动处理过时的哈希格式
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

#定义函数verify_password，接受明文密码和哈希密码作为参数，返回一个布尔值，表示密码是否匹配
#会将明文密码进行同样 的哈希运算，然后与数据库中的哈希值进行比对，正确返回True，错误返回False
def verify_password(plain_password:str,hashed_password:str)-> bool:
    return pwd_context.verify(plain_password,hashed_password)
#定义函数get_password_hash，接受一个明文密码作为参数，返回该密码的哈希值
#自动生成随机的盐与密码混合，经过复杂的运算生成一个安全的哈希字符串，防止彩虹攻击
def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

#定义函数create_access_token，接受一个数据字典和一个可选的过期时间参数，返回一个JWT访问令牌字符串
#
def create_access_token(data:dict,expires_delta:Optional[timedelta]=None) ->str:
    to_encode = data.copy()
    #复制一份传入的宝典，避免修改原字典影响函数外部的数据，使用.copy()是为了保护原始数据
    expire = datetime.utcnow() +(expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES) )#计算Token的过期时间
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,settings.SECRET_KEY,algorithm="HS256")
    #指定签名算法为HMAC-SHA256,会生成长字符串
