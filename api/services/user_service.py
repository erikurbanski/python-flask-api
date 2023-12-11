from ..entites.user import User
from ..models import user_model
from api import db

def create_user(user: User):
    user_db = user_model.User(
        name=user.name,
        email=user.email,
        password=user.password,
        is_admin=user.is_admin,
        api_key=user.api_key
    )
    user_db.encrypt()
    db.session.add(user_db)
    db.session.commit()

    return user_db

def get_user_by_email(email: str):
    return user_model.User.query.filter_by(email=email).first()

def get_user_by_id(id: int):
    return user_model.User.query.filter_by(id=id).first()


def get_user_by_api_key(api_key: str):
    return user_model.User.query.filter_by(api_key=api_key).first()