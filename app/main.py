import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import user, authentication, socket

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(user.router, tags=['user'])
app.include_router(authentication.router, tags=['authenticate'])
app.include_router(socket.router, tags=['web-scoket'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
