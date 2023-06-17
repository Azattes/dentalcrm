import datetime
from typing import Optional

import ormar
from users.types import AppointmentStatusType, RoleType

from dentalcrm.dependencies import get_database, get_metadata


class BaseMeta(ormar.ModelMeta):
    database = get_database()
    metadata = get_metadata()


class User(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    surname: str = ormar.String(max_length=150)
    name: str = ormar.String(max_length=150)
    patronymic: str = ormar.String(max_length=150)
    email: str = ormar.String(max_length=255, unique=True)
    role: str = ormar.String(
        choices=RoleType, max_length=15, default=RoleType.patient
    )
    password: str = ormar.String(max_length=255)

    class Meta(BaseMeta):
        tablename = "users"
        constaints = [ormar.UniqueColumns("email")]


class Schedule(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    date: datetime.date = ormar.Date()
    start_time: datetime.time = ormar.Time()
    end_time: datetime.time = ormar.Time()
    user: Optional[User] = ormar.ForeignKey(User)

    class Meta(BaseMeta):
        tablename = "schedules"
        constraints = [ormar.UniqueColumns("date", "user")]


class Appointment(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    doctor: int = ormar.ForeignKey(User, related_name="doctor")
    schedule: int = ormar.ForeignKey(Schedule)
    patient: int = ormar.ForeignKey(User, related_name="patient")
    status: str = ormar.String(
        choices=AppointmentStatusType,
        max_length=15,
        default=AppointmentStatusType.scheduled,
    )

    class Meta(BaseMeta):
        tablename = "appointments"
