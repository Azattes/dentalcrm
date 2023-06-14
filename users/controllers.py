from datetime import date

from fastapi import APIRouter, HTTPException
from ormar.exceptions import NoMatch
from users.models import Appointment, Schedule, User

router = APIRouter()


@router.post(
    path="/users/", tags=["users"], response_model=User, status_code=201
)
async def create_user(data: User):
    instance = await data.save()
    return instance


@router.get(path="/users/", tags=["users"], status_code=200)
async def get_users(role: str = None):
    if role:
        instance = await User.objects.filter(role=role).all()
        return instance
    instance = await User.objects.all()
    return instance


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
