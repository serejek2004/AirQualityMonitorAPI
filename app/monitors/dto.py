from dataclasses import dataclass


@dataclass
class MonitorsDTO:
    co2: int
    temperature: int
    humidity: int

    @classmethod
    def from_request(cls, data):
        return cls(
            co2=data['co2'],
            temperature=data['temperature'],
            humidity=data['humidity'],
        )
