from app.database.models.bloodRequestModel import BloodRequest
from app.core.exceptions import ValidationException,DuplicateException
import logging
import uuid
from mongoengine.errors import NotUniqueError

logger = logging.getLogger(__name__)

def create_blood_request(request_data):
    if not request_data:
        raise ValidationException("Blood request data is required")
    
    try:
        request_id = str(uuid.uuid4())   

        blood_request = BloodRequest(
            request_id=request_id,
            **request_data
        )
        blood_request.save()
        serialized_request = blood_request.to_json()
        return serialized_request

    except NotUniqueError:
        raise DuplicateException("Duplicate blood request")
  

def get_blood_request_by_id(request_id: str):
    try:
        if not request_id:
            raise ValidationException("Request ID is required")
        blood_request = BloodRequest.objects.get(request_id=request_id)
        return blood_request
    except BloodRequest.DoesNotExist:
        raise NotFoundException("Blood request not found")


def update_blood_request(request_id: str, data: dict):
    try:
        if not request_id:
            raise ValidationException("Request ID is required")
        blood_request = BloodRequest.objects.get(request_id=request_id)
        blood_request.update(**data)
        return blood_request
    except BloodRequest.DoesNotExist:
        raise NotFoundException("Blood request not found")


