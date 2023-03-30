from fastapi import APIRouter
from users.models import User
from users.schemas import UserSchema


router = APIRouter()


@router.post(path="/users/")
async def create_user(data: UserSchema):
    user = await User.objects.create(
        surname=data.surname,
        name=data.name,
        patronymic=data.patronymic,
        email=data.email,
        role=data.role,
        password=data.password,
    )
    return user
