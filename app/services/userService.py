from app.core.exceptions import ValidationException, DuplicateException
from app.database.models.userModel import User
from mongoengine.errors import NotUniqueError
import logging
import uuid

logger = logging.getLogger(__name__)


def create_user(data: dict):
    try:
        if not data:
            raise ValidationException("User data is required")

        user = User(**data)
        user.save()

        return user
    except NotUniqueError:
        raise DuplicateException("User Email or Mobile already exists")




  
