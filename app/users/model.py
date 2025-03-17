from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash

users_has_monitors = db.Table(
    'UsersHasMonitors',
    db.Column('users_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('monitors_id', db.Integer, db.ForeignKey('monitors.id'), primary_key=True)
)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    co2_max = db.Column(db.Integer, nullable=False, default=0)
    co2_min = db.Column(db.Integer, nullable=False, default=0)
    temperature_max = db.Column(db.Integer, nullable=False, default=0)
    temperature_min = db.Column(db.Integer, nullable=False, default=0)
    humidity_max = db.Column(db.Integer, nullable=False, default=0)
    humidity_min = db.Column(db.Integer, nullable=False, default=0)
    monitors = db.relationship('Monitors', secondary=users_has_monitors, back_populates='users')

    def __repr__(self) -> str:
        return f"User email: {self.email}"

    def set_password(self, password) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "co2_max": self.co2_max,
            "co2_min": self.co2_min,
            "temperature_max": self.temperature_max,
            "temperature_min": self.temperature_min,
            "humidity_max": self.humidity_max,
            "humidity_min": self.humidity_min
        }
