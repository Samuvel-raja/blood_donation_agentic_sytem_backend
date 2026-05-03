from app.services.bloodRequestService import create_blood_request

class BloodRequestController:
    def create_blood_request_controller(self, request_data):
        blood_request = create_blood_request(request_data)
        return {
            "id": str(blood_request.id),
            "patient_name": blood_request.patient_name,
            "blood_group": blood_request.blood_group,
            "quantity": blood_request.quantity,
            "status": blood_request.status
        }

