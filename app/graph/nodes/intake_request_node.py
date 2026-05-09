from app.services.bloodRequestService import create_blood_request
from app.services.notificationService import NotificationService
from app.services.googleMapService import HospitalVerificationService
from app.core.exceptions import ValidationException

import logging

logger = logging.getLogger(__name__)
notification_service = NotificationService()
hospital_verification_service = HospitalVerificationService()

from app.graph.states.state import BloodRequestState


async def intake_request_node(state: BloodRequestState):
    request_data = state.request_data
    res = create_blood_request(request_data)

    
    # blood_request = create_blood_request(state)
    # res =await hospital_verification_service.verify_hospital("Apollo hospital", "Chennai")
    # await notification_service.send_email_blood_alert("samuvelraja072@gmail.com", "A+", "Apollo hospital")

    return {
        "request_id": res.get("request_id",""),
        "responses": [res],
    }

def last_node(state: BloodRequestState):
    return {
        "status": "completed",
        "state": state
    }
    