import os
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
from user.router import router as login_router

load_dotenv()

app = FastAPI()

app.include_router(login_router)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('SERVER_HOST'), port=int(os.getenv('SERVER_PORT')))