from fast_zero.schemas import UserPublic
from tests.factories import UserFactory


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_users_with_users(session, client):
    users = UserFactory.create_batch(10)
    session.bulk_save_objects(users)
    session.commit()

    users_schema = [
        UserPublic.model_validate(user).model_dump() for user in users
    ]

    response = client.get('/users/')
    assert response.json() == {'users': users_schema}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': user.id,
    }


def test_update_user_with_wrong_user(client, user2, token):
    response = client.put(
        f'/users/{user2.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_wrong_user(client, user2, token):
    response = client.delete(
        f'/users/{user2.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}


def test_create_user_two_time(client):
    json = {
        'username': 'alice',
        'email': 'alice@example.com',
        'password': 'secret',
    }
    client.post('/users/', json=json)
    response = client.post('/users/', json=json)

    assert response.status_code == 400
    assert response.json() == {'detail': 'Email already registered'}
