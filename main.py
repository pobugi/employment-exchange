import uvicorn

from typing import Optional
from fastapi import FastAPI
from db.base import database
from endpoints import users

app = FastAPI(title="Employment Exchange")
app.include_router(users.router, prefix="/user", tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()
    
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True) 