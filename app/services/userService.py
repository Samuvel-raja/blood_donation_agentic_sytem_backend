from app.core.exceptions import ValidationException, DuplicateException, NotFoundException
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

def get_user_by_id(user_id: str):
    try:
        if not user_id:
            raise ValidationException("User ID is required")
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        raise NotFoundException("User not found")


def update_user(user_id: str, data: dict):
    try:
        if not user_id:
            raise ValidationException("User ID is required")
        user = User.objects.get(id=user_id)
        user.update(**data)
        return user
    except User.DoesNotExist:
        raise NotFoundException("User not found")


def get_users_by_fields(blood_group):
    try:
        users = User.objects(blood_group=blood_group)
        serialized_users = [

            user.to_json()

            for user in users
        ]

        return serialized_users
        
    except User.DoesNotExist:
        raise NotFoundException("Users not found")





  
