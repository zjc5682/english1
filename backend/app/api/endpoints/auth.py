#APIRouter用于创建一个路由器对象，将相关路由分组
# ，Depends用于依赖注入，
# HTTPException用于抛出http错误响应
from fastapi import APIRouter,Depends,HTTPException,status

#sqlmodel的Session用于数据库会话，selcect用于构建查询数据的语句
from sqlmodel import Session,select

from app.core.security import verify_password,get_password_hash,create_access_token
from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserCreate,UserRead,Token
from app.api.dependencies import get_current_user

#实例化一个API路由器，设置前缀为/auth，标签为authentication，用于处理与认证相关的API端点
router = APIRouter(prefix="/auth",tags=["authentication"])

#定义post请求的接口，路径为/register,响应数据格式为UserRead，状态码为201创建成功
@router.post("/register",response_model = UserRead,status_code=status.HTTP_201_CREATED)
#user_in:UserCreate表示将请求体的JSON 数据解析为UserCreate对象，session:Session = Depends(get_session)表示依赖注入一个数据库会话对象
def register(user_in:UserCreate,session:Session = Depends(get_session)):
    existing_user = session.exec(select(User).where(User.username == user_in.username)).first()#first()获取第一条结果
    if existing_user:
        raise HTTPException(status_code=400,detail="用户名已被注册")
    
    existing_email = session.exec(select(User).where(User.email == user_in.email)).first()
    if existing_email:
        #抛出异常，状态码400表示请求错误，detail提供错误信息
        raise HTTPException(status_code=400,detail="邮件已被注册")
    
    #创建一个新的User数据库模型实例
    user  =User(
        username = user_in.username,
        email = user_in.email,
        hashed_password = get_password_hash(user_in.password),#将明文密码进行哈希加密后存储，绝不存储明文密码
        is_active = True,   #设置用户为活跃状态，允许登录
    )
    session.add(user)#将新用户对象添加到数据库会话中，准备进行数据库操作
    session.commit()#提交事务，将更改真正写入数据库
    session.refresh(user)#刷新用户对象，使其包含数据库生成的字段
    return user         #返回新创建的用户对象

@router.post("/login",response_model=Token)
#定义登录函数，接受用户名和密码作为参数，并依赖注入一个数据库会话对象
def login(credentials:UserCreate,session:Session = Depends(get_session)):
    user = session.exec(
        select(User).where(
            (User.username == credentials.username) |(User.email == credentials.email)
        )
    ).first()#根据用户名或邮箱查询用户对象
    if not user or not verify_password(credentials.password,user.hashed_password):
        raise HTTPException(status_code=401,detail="用户名或密码错误")
    access_token = create_access_token(data={"sub":user.username})#创建一个JWT访问令牌，包含用户的用户名作为主题
    return{"access_token":access_token,"token_type":"bearer"}   #返回访问令牌和令牌类型，供前端使用


#定义一个GET请求接口，路劲为/me，响应数据格式为UserRead
@router.get("/me",response_model= UserRead)
def read_current_user(current_user:User = Depends(get_current_user)):
    #get_current_user是一个依赖函数，会自动解析请求头中的Token，验证用户身份，返回用户对象中
    return current_user