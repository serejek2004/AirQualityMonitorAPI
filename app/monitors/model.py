from app.database import db
from app.users.model import users_has_monitors


class Monitors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    co2 = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    users = db.relationship('Users', secondary=users_has_monitors, back_populates='monitors')

    def __repr__(self) -> str:
        return f"id: {self.id}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "co2": self.co2,
            "temperature": self.temperature,
            "humidity": self.humidity,
        }
