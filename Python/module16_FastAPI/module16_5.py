from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User was not found")

    user = users[user_id - 1]
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post("/user/{username}/{age}")
async def add_user(username: str = Path(min_length=5,
                                        max_length=20,
                                        description="Enter username",
                                        example="UrbanUser"),
                   age: int = Path(ge=18,
                                   le=120,
                                   description="Enter age",
                                   example="24")
                   ) -> User:
    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int,
                      username: str = Path(min_length=5,
                                           max_length=20,
                                           description="Enter username",
                                           example="UrbanUser"),
                      age: int = Path(ge=18,
                                      le=120,
                                      description="Enter age",
                                      example="24")
                      ) -> User:
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User was not found")

    users[user_id - 1].username = username
    users[user_id - 1].age = age
    return users[user_id - 1]


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User was not found")

    deleted_user = users.pop(user_id - 1)
    return deleted_user
