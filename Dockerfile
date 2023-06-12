# Указываем базовый образ
FROM python:3.10-slim

# Устанавливаем poetry
RUN pip install poetry

# Копируем файлы проекта в контейнер
WORKDIR /app
COPY . /app

# Устанавливаем зависимости с помощью poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Указываем команду для запуска приложения
CMD bash start.sh
