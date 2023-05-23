import dataclasses
import datetime
from enum import Enum


class UserGender(Enum):
    Male = 1
    Female = 2
    Other = 3


class UserHobby(Enum):
    Sports = 1
    Reading = 2
    Music = 3


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: UserGender
    phone: str
    date_of_birth: datetime.date
    subject: str
    hobby: UserHobby
    picture: str
    address: str
    state: str
    city: str


student = Users(
    first_name="Helen",
    last_name="Morilova",
    email="test@test.ru",
    gender=UserGender.Female,
    phone="5555555555",
    date_of_birth=datetime.date(1984, 5, 12),
    subject="Arts",
    hobby=UserHobby.Sports,
    picture="404-img.png",
    address="adress street, 1",
    state="NCR",
    city="Delhi",
)