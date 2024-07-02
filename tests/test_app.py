from http import HTTPStatus


# Arrange (Organização)
def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Garantir)
    assert response.json() == {'message': 'Olá mundo!'}  # Assert (Garantir)


def test_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'username',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # Voltou o statusc_code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'username',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'username',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        }
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
# def test_read_root_quiz_retornar_ok_html():
#    client = TestClient(app)
#    response = client.get('/quiz')
#
#    assert response.status_code == HTTPStatus.OK
#    assert response.text == """<html><body><p>Olá mundo</p></body></html>"""
