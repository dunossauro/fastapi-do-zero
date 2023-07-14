from freezegun import freeze_time


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_token_inexistent_user(client):
    response = client.post(
        '/token',
        data={'username': 'no_user@no_domain.com', 'password': 'testtest'},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_token_wrong_password(client, user):
    response = client.post(
        '/token', data={'username': user.email, 'password': 'wrong_password'}
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_refresh_token(client, user, token):
    response = client.post(
        '/refresh_token',
        headers={'Authorization': f'Bearer {token}'},
    )

    data = response.json()

    assert response.status_code == 200
    assert 'access_token' in data
    assert 'token_type' in data
    assert response.json()['token_type'] == 'bearer'


def test_token_expiry(client, user):
    with freeze_time('2023-07-14 12:00:00'):
        response = client.post(
            '/token',
            data={'username': user.email, 'password': user.clean_password},
        )
        assert response.status_code == 200
        token = response.json()['access_token']

    with freeze_time('2023-07-14 13:00:00'):
        response = client.post(
            '/refresh_token',
            headers={'Authorization': f'Bearer {token}'},
        )
        assert response.status_code == 401
        assert response.json() == {'detail': 'Could not validate credentials'}
