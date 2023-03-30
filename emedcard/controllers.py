import uuid
from datetime import date

import aiofiles
from emedcard.models import Xray
from fastapi import APIRouter, File, Form, UploadFile

router = APIRouter(prefix="/e-med-card")


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
