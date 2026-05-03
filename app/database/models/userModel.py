from mongoengine import Document,StringField,DateTimeField,ListField
from datetime import datetime, timezone

class User(Document):
    name = StringField(required=True)
    mobile = StringField(required=True,max_length=10,unique=True)
    email = StringField(required=True,unique=True)
    date_of_birth = DateTimeField(required=True)
    blood_group = StringField(required=True,choices=("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"))
    roles = ListField(
        StringField(choices=("donor", "recipient", "admin")),
        default=lambda: ["donor"],
        min_length=1
    )
    last_donation_date = DateTimeField(required=False,null=True)
    created_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    meta = {
        "indexes": [
            "email",
            "mobile",
            "blood_group"
        ]
    }
    