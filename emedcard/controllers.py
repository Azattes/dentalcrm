import uuid
from pathlib import Path
from typing import List

import aiofiles
from emedcard.models import Allergy, Disease, EMedCard, Xray
from emedcard.schemas import CreateEMedCardSchema
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse
from users.models import User

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent


@router.post(path="/xray/", tags=["x-ray"])
async def create_xray(
    comment: str = Form(),
    patient: int = Form(),
    image: UploadFile = File(),
):
    filename = f"{uuid.uuid4()}.jpg"

    async with aiofiles.open(f"media/{filename}", "wb") as f:
        content = await image.read()
        await f.write(content)

    image_url = f"/api/xray-image/?image={filename}"
    xray = await Xray.objects.create(
        image_url=image_url,
        comment=comment,
        patient=patient,
    )

    return xray


@router.get(path="/xray-image/", tags=["x-ray"])
async def get_xray_image(image: str):
    image_full_path = BASE_DIR / "media" / image

    # Проверка существования файла
    if not image_full_path.is_file():
        raise FileNotFoundError

    # Возвращение фотографии в виде FileResponse
    return FileResponse(image_full_path)


@router.delete(path="/xray/", tags=["x-ray"], status_code=200)
async def get_xray(xray_id: int):
    xrays = await Xray.objects.delete(id=xray_id)
    return xrays


@router.get(path="/xray/", tags=["x-ray"], status_code=200)
async def get_xray(patient: int):
    xrays = await Xray.objects.filter(patient=patient).all()
    return xrays


@router.post(path="/e-med-card/", tags=["e-med-card"], status_code=201)
async def create_emedcard(data: CreateEMedCardSchema):
    await Disease.objects.get_or_create(name=data.disease)
    instance = await EMedCard.objects.create(
        patient=data.patient,
        doctor=data.doctor,
        disease=data.disease,
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
    allergy = await Allergy.objects.filter(user=patient.id).all()
    return allergy


@router.get(path="/e-med-card/", tags=["e-med-card"], status_code=200)
async def get_emedcard(patient_id: int):
    patient = await User.objects.get(id=patient_id)
    emedcard = (
        await EMedCard.objects.select_related(["doctor", "patient"])
        .filter(patient=patient.id)
        .all()
    )
    return emedcard
