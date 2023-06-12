from datetime import date

import ormar
from users.models import User

from dentalcrm.dependencies import get_database, get_metadata


class BaseMeta(ormar.ModelMeta):
    database = get_database()
    metadata = get_metadata()


class Disease(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255)

    class Meta(BaseMeta):
        tablename = "disease"


class EMedCard(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    patient: int = ormar.ForeignKey(
        User,
        ondelete=ormar.ReferentialAction.CASCADE,
        nullable=False,
        related_name="emedcard_patient",
    )
    disease: int = ormar.ForeignKey(Disease, nullable=True)
    date: date = ormar.Date(default=date.today())
    treatment: str = ormar.Text()
    doctor: int = ormar.ForeignKey(
        User,
        ondelete=ormar.ReferentialAction.CASCADE,
        nullable=False,
        related_name="emedcard_doctor",
    )

    class Meta(BaseMeta):
        tablename = "e_med_card"


class Allergy(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    user: int = ormar.ForeignKey(User)
    allergen: str = ormar.String(max_length=255)
    description: str = ormar.Text()

    class Meta(BaseMeta):
        tablename = "allergy"


class Xray(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    patient: int = ormar.ForeignKey(User, related_name="xray.patient")
    date: date = ormar.Date()
    comment: str = ormar.Text()
    image_url: str = ormar.String(max_length=255)

    class Meta(BaseMeta):
        tablename = "xrays"
