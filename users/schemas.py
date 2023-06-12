from datetime import date

from pydantic import BaseModel


class UserSchema(BaseModel):
    surname: str
    name: str
    patronymic: str
    email: str
    role: str
    password: str


class ReadScheduleSchema(BaseModel):
    doctor_id: int
    date: date
