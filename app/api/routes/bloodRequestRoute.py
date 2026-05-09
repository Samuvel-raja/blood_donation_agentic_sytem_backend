from fastapi import APIRouter
from app.api.controllers.bloodRequestController import BloodRequestController
from app.graph.graph import graph

router = APIRouter()
controller = BloodRequestController()

@router.post("/blood-request")
async def create_blood_request(request_data: dict):
    initial_state = {
        "request_id": "",

        "request_data": {},

        "donors": [],
        "batch": [],
        "responses": [],

        "accepted_donor": None,

        "hospital_verification_data": {},

        "current_batch": 0,
        "max_batches": 0,

        "status": ""
    }
    state = initial_state
    state["request_data"] = request_data
   
    result = await graph.ainvoke(state)
    return result