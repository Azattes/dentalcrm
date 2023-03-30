from datetime import date

from fastapi import File
from pydantic import BaseModel


class CreateXraySchema(BaseModel):
    patient: int
    date: date
    comment: str
    image: str
