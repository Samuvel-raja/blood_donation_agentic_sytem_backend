from mongoengine import connect
from config import settings


def init_db():
    connect(
        db=settings.mongo_db,
        host=settings.mongo_uri
    )
    print("Database connected successfully")