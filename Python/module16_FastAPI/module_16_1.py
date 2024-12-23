from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return "Это главная страница"


@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user_post(username: str, age: int = 54):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

