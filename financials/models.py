from datetime import date, datetime

import ormar
from users.models import User

from dentalcrm.dependencies import get_database, get_metadata


class BaseMeta(ormar.ModelMeta):
    database = get_database()
    metadata = get_metadata()


class Accounting(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    admin: int = ormar.ForeignKey(User, related_name="admin")
    patient: int = ormar.ForeignKey(User, related_name="patient")
    date: datetime = ormar.DateTime(default=datetime.now())
    paid_amount: int = ormar.Integer()
    desctiption: str = ormar.Text()

    class Meta:
        tablename = "accounting"


class ProfitLoss(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    start_date: date = ormar.Date()
    end_date: date = ormar.Date()
    total_income: float = ormar.Float(default=0)
    total_expenses: float = ormar.Float(default=0)
    total: float = ormar.Float(default=0)

    class Meta:
        tablename = "profit_loss"


class Loss(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    loss: float = ormar.Float(default=0)
    date: date = ormar.Date(default=datetime.now())
    description: str = ormar.Text()

    class Meta:
        tablename = "loss"
