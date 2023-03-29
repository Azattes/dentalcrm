from functools import lru_cache
from dentalcrm.settings import Settings
from databases import Database
from sqlalchemy import MetaData


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def get_database():
    settings = get_settings()
    return Database(url=settings.database_url)


@lru_cache
def get_metadata():
    return MetaData
