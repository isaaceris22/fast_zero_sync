from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)                          # Arrange (Organização)
    response = client.get('/')                          # Act (Ação)

    assert response.status_code == HTTPStatus.OK        # Assert (Garantir)
    assert response.json() == {'message': 'Olá mundo!'}  # Assert (Garantir)

# def test_read_root_quiz_retornar_ok_html():
#    client = TestClient(app)
#    response = client.get('/quiz')
#
#    assert response.status_code == HTTPStatus.OK
#    assert response.text == """<html><body><p>Olá mundo</p></body></html>"""
