from enum import Enum


class RoleType(str, Enum):
    doctor = "Врач"
    patient = "Пациент"
    admin = "Администратор"
