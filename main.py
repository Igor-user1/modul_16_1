import uvicorn
from fastapi import FastAPI, encoders

app = FastAPI()

@app.get('/')
async def main():
    return 'Главная страница'

@app.get('/user/admin')
async def admin():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def user_num(user_id: int):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user')
async def admin(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)