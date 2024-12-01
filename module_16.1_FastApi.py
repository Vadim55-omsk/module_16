from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/user/{user_id}")
async def get_user_id(user_id: int):
    return f"Вы вошли как пользователь №{user_id}"


@app.get("/user")
async def get_user_info(username: str = 'Timmi', age: int = 34):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"