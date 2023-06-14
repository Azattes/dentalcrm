from datetime import date, datetime, timedelta


async def get_date_range_inclusive(start_date: date, end_date: date):
    start_date = datetime(2023, 1, 1)  # Замените эту дату своим значением
    end_date = datetime(2023, 2, 1)  # Замените эту дату своим значением

    delta = end_date - start_date
    dates = []

    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        dates.append(date)

    return dates
