from flask_sqlalchemy import SQLAlchemy
from app.users.model import Users


class UserDAO:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_by_email(self, email: str) -> Users | None:
        return self.db.session.query(Users).filter_by(email=email).first()

    def register(self, user: Users) -> Users:
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def update(self, updated_user: Users) -> Users | None:
        user = self.db.session.query(Users).filter_by(email=updated_user.email).first()

        if user:
            user.co2_max = updated_user.co2_max
            user.co2_min = updated_user.co2_min
            user.temperature_max = updated_user.temperature_max
            user.temperature_min = updated_user.temperature_min
            user.humidity_max = updated_user.humidity_max
            user.humidity_min = updated_user.humidity_min

            self.db.session.commit()
            return user

        return None

