from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

from app.config.settings import get_settings
from app.db import db
from app.models.user import UserModel

from app.db.users import UserDBManager

config = get_settings()
app = FastAPI(title=config.app_title)


@app.on_event("startup")
async def startup():
    await db.open_db_connection()


@app.on_event("shutdown")
async def shutdown():
    await db.close_db_connection()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.post("/register", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):
    user_dict = user.dict()
    # foo = await db.from_collection(UserDBManager()).create_user(user_dict)
    # Users will be its own module/routes file. This will be a class that then uses
    # the from_collection method in its __init__ method.
    # This will then allow specific user db methods to be used from another file.
    # foo = await db.from_collection(UserDBManager)
    # a = await db.collection.create_user()
    # foo = await db.from_collection(UserDBManager).create_user()
    # a = await foo.create_user()
    a = await db(UserDBManager).create_user(user_dict)
    # print(user_dict)
    # new_user = await db.collection("users".insert_one(user_dict)
    # new_user = db.collection("users").insert_one(user_dict)
    # new_user = await db["users"].insert_one(user_dict)
    # new_user = await db.create_user(user_dict)
    # print(new_user)
    # print(dir(new_user))
    # created_user = await db.collection("users").find_one({"_id": new_user.inserted_id})
    # print(created_user)

    return JSONResponse(status_code=201, content={"message": "done"})
