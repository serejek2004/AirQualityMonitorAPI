from dataclasses import dataclass


@dataclass
class AuthUsersDTO:
    email: str
    password: str

    @classmethod
    def from_request(cls, data):
        return cls(
            email=data["email"],
            password=data["password"]
        )


@dataclass
class UpdateUsersDTO:
    email: str
    co2_max: int
    co2_min: int
    temperature_max: int
    temperature_min: int
    humidity_max: int
    humidity_min: int

    @classmethod
    def from_request(cls, data):
        return cls(
            email=data["email"],
            co2_max=data.get("co2_max"),
            co2_min=data.get("co2_min"),
            temperature_max=data.get("temperature_max"),
            temperature_min=data.get("temperature_min"),
            humidity_max=data.get("humidity_max"),
            humidity_min=data.get("humidity_min"),
        )
