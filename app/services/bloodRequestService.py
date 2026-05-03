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
        return blood_request

    except NotUniqueError:
        raise DuplicateException("Duplicate blood request")
  
