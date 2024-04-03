from fastapi import FastAPI

app = FastAPI()


@app.post('/users/')
def create_user():
    ...


from http import HTTPStatus

# ...

@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user():
    ...


from fast_zero.schemas import Message, UserSchema

# ...

@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    ...


from fast_zero.schemas import Message, UserSchema, UserPublic

# Código omitido

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    ...


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user


from fast_zero.schemas import Message, UserSchema, UserPublic, UserDB

# código omitido

database = []  # Lista provisória para fins de estudo

# código omitido

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)  #(1)!

    database.append(user_with_id)

    return user_with_id


from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

# código omitido

@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


from fastapi import FastAPI, HTTPException

# ...

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1: #(1)!
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        ) #(2)!

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id #(3)!

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}
