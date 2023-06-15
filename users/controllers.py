from datetime import date

from asyncpg import UniqueViolationError
from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from ormar.exceptions import NoMatch
from users.models import Appointment, Schedule, User
from users.schemas import LoginSchema

from dentalcrm.exceptions import NotFoundException

router = APIRouter()


@router.post(path="/users/", tags=["users"], status_code=201)
async def create_user(data: User):
    try:
        instance = await data.save()
    except UniqueViolationError:
        return {"detail": "User with this email already exist"}
    return instance


@router.get(path="/users/", tags=["users"], status_code=200)
async def get_users(role: str = None):
    if role:
        instance = await User.objects.filter(role=role).all()
        return instance
    instance = await User.objects.all()
    return instance


@router.get(path="/get-users/", tags=["users"], status_code=200)
async def get_users_by_token(Authorize: AuthJWT = Depends()):
    current_user = Authorize.get_jwt_subject()
    user = await User.objects.get(email=current_user)
    return user


@router.get(path="/schedule/", tags=["schedule"], response_model=Schedule)
async def get_schedule(doctor_id: int, date: date):
    try:
        schedule = await Schedule.objects.select_related("appointments").get(
            user=doctor_id, date=date
        )
    except NoMatch:
        raise HTTPException(status_code=404, detail="Not found")
    return schedule


@router.post(
    path="/schedule/",
    tags=["schedule"],
    response_model=Schedule,
    status_code=201,
)
async def create_schedule(data: Schedule):
    schedule = await data.save()
    return schedule


@router.post(path="/schedule/appointment/", tags=["schedule"], status_code=201)
async def create_appointment(data: Appointment):
    instance = await data.save()
    return instance


@router.post(path="/auth/login/", tags=["auth"])
async def login(data: LoginSchema, Authorize: AuthJWT = Depends()):
    try:
        user = await User.objects.get(email=data.email)
    except NoMatch:
        raise NotFoundException
    if user.email == data.email and user.password == data.password:
        access_token = Authorize.create_access_token(subject=data.email)
        refresh_token = Authorize.create_refresh_token(subject=data.email)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    return {"detail": "Incorrect authorization data"}


@router.post(path="/auth/refresh/", tags=["auth"])
def refresh(Authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}
