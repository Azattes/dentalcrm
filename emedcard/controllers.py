import uuid
from datetime import date

import aiofiles
from emedcard.models import EMedCard, Xray
from fastapi import APIRouter, File, Form, UploadFile
from users.models import User

router = APIRouter()


@router.post(path="/xray/", tags=["x-ray"])
async def create_xray(
    date: date = Form(),
    comment: str = Form(),
    patient: int = Form(),
    image: UploadFile = File(),
):
    filename = f"{uuid.uuid4()}.jpg"

    async with aiofiles.open(f"media/{filename}", "wb") as f:
        content = await image.read()
        await f.write(content)

    image_url = f"/media/{filename}"
    xray = await Xray.objects.create(
        image_url=image_url,
        date=date,
        comment=comment,
        patient=patient,
    )

    return xray


@router.get(path="/xray/", tags=["x-ray"], status_code=200)
async def get_xray(date: date, patient):
    xrays = await Xray.objects.filter(data=date, patient=patient).all()
    return xrays


@router.post(path="/e-med-card/", tags=["e-med-card"], status_code=201)
async def create_emedcard(data: EMedCard):
    instance = await data.save()
    return instance


@router.get(path="/e-med-card/", tags=["e-med-card"], status_code=200)
async def get_emedcard(patient_id: int):
    patient = await User.objects.get(id=patient_id)
    return patient
