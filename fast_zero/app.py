from http import HTTPStatus

from fastapi import FastAPI, HTTPException

# from fastapi.responses import HTMLResponse
from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

databese = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(databese) + 1, **user.model_dump())

    databese.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': databese}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(databese) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(id=user_id, **user.model_dump())

    databese[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(databese) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del databese[user_id - 1]

    return {'message': 'User deleted'}
# @app.get('/quiz', status_code=HTTPStatus.OK, response_class=HTMLResponse)
# def read_quiz():
#    return """<html><body><p>Olá mundo</p></body></html>"""
