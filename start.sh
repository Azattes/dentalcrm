alembic upgrade head &&
uvicorn --host=0.0.0.0 --port=8000 dentalcrm.asgi:app --reload