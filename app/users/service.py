from flask_sqlalchemy import SQLAlchemy
from app.users.dao import UserDAO
from app.users.model import Users
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
import re


def is_valid_email(email):
    return re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email)


class UserService:
    def __init__(self, db: SQLAlchemy):
        self.dao = UserDAO(db)

    def register(self, new_user: Users) -> tuple[None, int] | tuple[Users, int]:

        user_from_db = self.dao.get_by_email(new_user.email)

        if not is_valid_email(new_user.email) or len(new_user.email) > 80 or user_from_db:
            return None, 409

        user_to_create = Users(email=new_user.email)
        user_to_create.set_password(new_user.password)

        user = self.dao.register(user_to_create)

        return user, 201

    def login(self, user_dto: Users) -> tuple[None, int] | tuple[str, int]:
        user = self.dao.get_by_email(user_dto.email)

        if not user:
            return None, 404

        if check_password_hash(user.password_hash, user_dto.password):
            access_token = create_access_token(identity=user.email)
            return access_token, 200
        else:
            return None, 403

    def update(self, user_dto: Users) -> tuple[None, int] | tuple[Users, int]:
        user = self.dao.update(user_dto)
        if user:
            return user, 200
        else:
            return None, 404
