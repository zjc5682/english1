from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # 关键：忽略 .env 中未定义的变量
    )
    
    PROJECT_NAME: str = "English Learning API"
    DATABASE_URL: str = "mysql+pymysql://张钧城:zjc123456@localhost:3306/zhan"
    SECRET_KEY: str = "change-me-to-a-random-secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()