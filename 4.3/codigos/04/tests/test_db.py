from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='alice', password='secret', email='teste@test')
    session.add(new_user)#(1)!
    session.commit()#(2)!

    user = session.scalar(select(User).where(User.username == 'alice'))#(3)!

    assert user.username == 'alice'
