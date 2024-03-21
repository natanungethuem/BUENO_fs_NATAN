from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserLogin(BaseModel):
    username: str
    password: str