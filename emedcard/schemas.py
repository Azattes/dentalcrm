from datetime import date

from fastapi import File
from pydantic import BaseModel


class CreateXraySchema(BaseModel):
    patient: int
    date: date
    comment: str


class CreateDiseaseSchema(BaseModel):
    name: str


class CreateEMedCardSchema(BaseModel):
    patient: int
    disease: int
    treatment: str
    doctor: int
    disease: CreateDiseaseSchema
