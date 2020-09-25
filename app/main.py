import uvicorn
from fastapi import FastAPI

from app.api import user, authentication

app = FastAPI()

app.include_router(user.router,tags=['user'])
app.include_router(authentication.router,tags=['authenticate'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
