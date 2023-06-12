from enum import Enum


class RoleType(str, Enum):
    doctor = "Врач"
    patient = "Пациент"
    admin = "Администратор"
    radiologist = "Рентгенолог"


class AppointmentStatusType(str, Enum):
    scheduled = "Записан"
    canceled = "Отменен"
    completed = "Завершено"
