from datetime import date

from fastapi import APIRouter
from financials.models import Accounting, Loss, ProfitLoss
from financials.services.get_date_range_inclusive import (
    get_date_range_inclusive,
)

router = APIRouter(prefix="/financials")


@router.post(path="/accounting/", tags=["financials"], status_code=201)
async def create_accounting(data: Accounting):
    instance = await data.save()
    return instance


@router.post(path="/loss/", tags=["financials"], status_code=201)
async def create_loss(data: Loss):
    instance = await data.save()
    return instance


@router.get(path="/total/", tags=["financials"], status_code=200)
async def get_total_net(start_date: date, end_date: date):
    date_range = await get_date_range_inclusive(
        start_date=start_date, end_date=end_date
    )
    profit = await Accounting.objects.filter(date__in=date_range).sum(
        "paid_amount"
    )
    loss = await Loss.objects.filter(date__in=date_range).sum("loss")
    if profit is None:
        profit = 0
    elif loss is None:
        loss = 0
    net = profit - loss
    await ProfitLoss.objects.create(
        start_date=start_date,
        end_date=end_date,
        total_income=profit,
        total_expenses=loss,
        total=net,
    )
    return {"total_profit": profit, "total_loss": loss, "total_net": net}
