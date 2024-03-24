import os
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn

from user.UserRouter import router as router_login
from order.OrderRouter import router as order_router

load_dotenv()

app = FastAPI()

app.include_router(router_login)
app.include_router(order_router)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('API_URL'),
                port=int(os.getenv('API_PORT')))
