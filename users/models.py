import ormar
from users.types import RoleType

from dentalcrm.dependencies import get_database, get_metadata


class BaseMeta(ormar.ModelMeta):
    database = get_database()
    metadata = get_metadata()


class User(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    surname: str = ormar.String(max_length=150)
    name: str = ormar.String(max_length=150)
    patronymic: str = ormar.String(max_length=150)
    email: str = ormar.String(max_length=255)
    role: str = ormar.String(
        choices=RoleType, max_length=10, default=RoleType.patient
    )
    password: str = ormar.String(max_length=255)

    class Meta(BaseMeta):
        tablename = "users"
        constaints = [ormar.UniqueColumns("email")]