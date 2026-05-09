from app.graph.states.state import BloodRequestState
from app.tools.googlemapTool import get_places_details
from app.database.models.bloodRequestModel import BloodRequest
from app.services.bloodRequestService import update_blood_request

async def hospital_verification_node(state: BloodRequestState):
    request_id = state.request_id

    request_data = state.request_data
    hospital_name = request_data.get("hospital_name", "")
    address = request_data.get("hospital_address", "")    
    hospital_data = await get_places_details(hospital_name, address)
    
    if hospital_data.get("verified",False):
        update_blood_request(request_id, {"is_hospital_verified": True})
    
    return {
        "hospital_verification_data": hospital_data,
    }

