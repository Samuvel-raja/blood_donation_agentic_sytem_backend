from mongoengine import Document, StringField, DateTimeField,ReferenceField,IntField,BooleanField
from datetime import datetime,timezone
from app.database.models.userModel import User

class BloodRequest(Document):
    request_id = StringField(required=True,unique=True)
    user = ReferenceField(User, required=True)
    patient_name = StringField(required=True)
    hospital = StringField(required=True)
    hospital_address = StringField(required=True)
    blood_group = StringField(required=True,choices=("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"))
    quantity = IntField(required=True,min_value=1)
    status = StringField(
        choices=("SEARCHING", "WAITING", "ASSIGNED", "FAILED"),
        default="SEARCHING"
    )
    created_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    is_hospital_verified = BooleanField(default=False)
    meta = {
        "indexes": [
            "user",
            {
                "fields": ["status", "blood_group"]
            },
            {
                "fields": ["hospital","is_hospital_verified"]
            }
        ]
    }
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(BloodRequest, self).save(*args, **kwargs)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "request_id": self.request_id,
            "user": str(self.user.id),
            "patient_name": self.patient_name,
            "hospital": self.hospital,
            "hospital_address": self.hospital_address,
            "blood_group": self.blood_group,
            "quantity": self.quantity,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_hospital_verified": self.is_hospital_verified
        }
    