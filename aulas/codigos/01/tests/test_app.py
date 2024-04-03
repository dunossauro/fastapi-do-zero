from fastapi.testclient import TestClient  # (1)!

from fast_zero.app import app  # (2)!

client = TestClient(app)  # (3)!


from http import HTTPStatus  # (6)!

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():  # (1)!
    client = TestClient(app)  # (2)!

    response = client.get('/')  # (3)!

    assert response.status_code == HTTPStatus.OK  # (4)!
    assert response.json() == {'message': 'Olá Mundo!'}  # (5)!


from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
