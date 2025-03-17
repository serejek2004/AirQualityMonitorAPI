from flask_sqlalchemy import SQLAlchemy
from app.monitors.model import Monitors


class MonitorDAO:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_monitor_by_id(self, id: int) -> Monitors | None:
        return self.db.session.query(Monitors).filter_by(id=id).first()

    def create_monitor(self, monitor: Monitors) -> Monitors:
        self.db.session.add(monitor)
        self.db.session.commit()
        return monitor

    def update_monitor_data(self, monitor_id: int, updated_monitor: Monitors) -> Monitors | None:
        monitor = self.db.session.query(Monitors).filter_by(id=monitor_id).first()

        if monitor:
            monitor.co2 = updated_monitor.co2
            monitor.temperature = updated_monitor.temperature
            monitor.humidity = updated_monitor.humidity

            self.db.session.commit()
            return monitor

        return None
