from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


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
async def update_user(user_id: int = Path(ge=1,
                                          le=100,
                                          description="Enter User ID",
                                          example="25"),
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
