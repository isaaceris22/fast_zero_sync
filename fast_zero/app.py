from http import HTTPStatus

from fastapi import FastAPI

# from fastapi.responses import HTMLResponse
from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}

# @app.get('/quiz', status_code=HTTPStatus.OK, response_class=HTMLResponse)
# def read_quiz():
#    return """<html><body><p>Olá mundo</p></body></html>"""
