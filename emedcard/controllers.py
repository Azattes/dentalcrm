import uuid
from datetime import date

import aiofiles
from emedcard.models import Allergy, Disease, EMedCard, Xray
from emedcard.schemas import CreateEMedCardSchema
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
async def create_emedcard(data: CreateEMedCardSchema):
    disease, _ = await Disease.objects.get_or_create(name=data.disease)
    instance = await EMedCard.objects.create(
        patient=data.patient,
        doctor=data.doctor,
        disease=disease.id,
        treatment=data.treatment,
    )
    return instance


@router.post(path="/allergy/", tags=["e-med-card"], status_code=201)
async def create_emedcard(data: Allergy):
    instance = await data.save()
    return instance


@router.get(path="/allergy/", tags=["e-med-card"], status_code=200)
async def get_emedcard(patient_id: int):
    patient = await User.objects.get(id=patient_id)
    allergy = await Allergy.objects.filter(patient=patient.id).all()
    return allergy


@router.get(path="/e-med-card/", tags=["e-med-card"], status_code=200)
async def get_emedcard(patient_id: int):
    patient = await User.objects.get(id=patient_id)
    emedcard = await EMedCard.objects.filter(patient=patient.id).all()
    return emedcard
