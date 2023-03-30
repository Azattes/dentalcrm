import os
import uuid

import aiofiles
from emedcard.models import Xray
from emedcard.schemas import CreateXraySchema
from fastapi import APIRouter

router = APIRouter(prefix="/e-med-card")


@router.post(path="/xray/", tags=["x-ray"])
async def create_xray(data: CreateXraySchema):
    filename = f"{uuid.uuid4()}.jpg"

    async with aiofiles.open(f"media/{filename}", "wb") as f:
        content = await data.image.read()
        await f.write(content)

    image_url = f"/media/{filename}"
    xray = await Xray.objects.create(
        image_url=image_url,
        date=data.date,
        comment=data.comment,
        patient=data.patient,
    )

    return xray
