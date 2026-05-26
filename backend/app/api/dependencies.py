from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from sqlmodel import Session,select
from app.core.config import settings
from app.db.session import get_session
from app.models.user import User
from app.schemas.user import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl ="/api/auth/login")

def get_current_user(
        token:str =Depends(oauth2_scheme),session:Session = Depends(get_session)) -> User:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "无法验证凭据",
        headers = {"WWW-Authenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])
        username:str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username = username)
    except JWTError:
        raise credentials_exception
    user = session.exec(select(User).where(User.username == token_data.username)).first()
    if user is None:
        raise credentials_exception
    return user
    