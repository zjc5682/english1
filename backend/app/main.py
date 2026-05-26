from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import words,auth
from app.db.session import engine
from app.db.base import SQLModel

app = FastAPI(title="English Learning API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(words.router, prefix="/api")
app.include_router(auth.router,prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to English Learning App API"}
