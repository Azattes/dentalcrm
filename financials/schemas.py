from datetime import date

from pydantic import BaseModel


class ProfilResponseSchema(BaseModel):
    total_income: float
    total_loss: float
    net_income: float
