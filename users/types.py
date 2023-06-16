from enum import Enum


class RoleType(str, Enum):
    doctor = "Врач"
    patient = "Пациент"
    admin = "Админ"
    radiologist = "Рентген"


class AppointmentStatusType(str, Enum):
    scheduled = "Записан"
    canceled = "Отменен"
    completed = "Завершено"
