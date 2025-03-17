from flask_sqlalchemy import SQLAlchemy
from app.monitors.dao import MonitorDAO
from app.monitors.model import Monitors


class MonitorService:
    def __init__(self, db: SQLAlchemy):
        self.dao = MonitorDAO(db)

    def register(self, monitor: Monitors) -> tuple[int, int]:
        monitor = self.dao.create_monitor(Monitors(co2=monitor.co2,
                                                   temperature=monitor.temperature,
                                                   humidity=monitor.humidity))

        return monitor.id, 201

    def update_monitor_data(self, monitor_id: int, monitor_data: Monitors) -> tuple[Monitors, int] | tuple[None, int]:
        monitor = self.dao.update_monitor_data(monitor_id, Monitors(co2=monitor_data.co2,
                                                                    temperature=monitor_data.temperature,
                                                                    humidity=monitor_data.humidity))

        if monitor:
            return monitor, 200
        else:
            return None, 404

    def get_data(self, id: int) -> tuple[None, int] | tuple[Monitors, int]:
        monitor = self.dao.get_monitor_by_id(id)

        if monitor:
            return monitor, 200
        else:
            return None, 404
