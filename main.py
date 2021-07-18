from fastapi import FastAPI

from app.config.settings import get_settings
from app.db import db


config = get_settings()
app = FastAPI(title=config.app_title)


@app.on_event("startup")
async def startup():
    await db.open_db_connection()


@app.on_event("shutdown")
async def shutdown():
    await db.close_db_connection()
