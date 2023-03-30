from pydantic import BaseModel


class UserSchema(BaseModel):
    surname: str
    name: str
    patronymic: str
    email: str
    role: str
    password: str
