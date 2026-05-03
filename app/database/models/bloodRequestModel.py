from mongoengine import Document, StringField, DateTimeField,ReferenceField,IntField
from datetime import datetime,timezone
from app.database.models.userModel import User

class BloodRequest(Document):
    request_id = StringField(required=True,unique=True)
    user = ReferenceField(User, required=True)
    patient_name = StringField(required=True)
    blood_group = StringField(required=True,choices=("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"))
    quantity = IntField(required=True,min_value=1)
    status = StringField(
        choices=("SEARCHING", "WAITING", "ASSIGNED", "FAILED"),
        default="SEARCHING"
    )
    created_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    meta = {
        "indexes": [
            "request_id",
            "user",
            {"fields": ["status", "blood_group"]}
        ]
    }