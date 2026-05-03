from app.services.bloodRequestService import create_blood_request
import logging

logger = logging.getLogger(__name__)

from app.graph.states.state import BloodRequestState

def intake_request_node(state: BloodRequestState):
    request_data = state.get("request_data", {})
    blood_request = create_blood_request(request_data)
    return {
        "request_id": str(blood_request.id)
    }

def last_node(state: BloodRequestState):
    return {
        "status": "completed",
        "state": state
    }
    