from mongoengine import Document,StringField,DateTimeField,ListField
from datetime import datetime, timezone

class User(Document):
    name = StringField(required=True)
    mobile = StringField(required=True,max_length=10,unique=True)
    email = StringField(required=True,unique=True)
    date_of_birth = DateTimeField(required=True)
    address = StringField(required=True)
    blood_group = StringField(required=True,choices=("A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"))
    roles = ListField(
        StringField(choices=("donor", "recipient", "admin")),
        default=lambda: ["donor"],
        min_length=1
    )
    last_donation_date = DateTimeField(required=False,null=True)
    status = StringField(required=True,choices=("active", "inactive"),default="active")
    created_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda:datetime.now(timezone.utc))
    meta = {
        "indexes": [
            {
                "fields": [
                    "blood_group",
                    "status",
                    "roles"
                ]
            },

            {
                "fields": [
                    "blood_group",
                    "status",
                    "last_donation_date"
                ]
            }
        ]
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(User, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "mobile": self.mobile,
            "email": self.email,
            "date_of_birth": self.date_of_birth,
            "address": self.address,
            "blood_group": self.blood_group,
            "roles": self.roles,
            "last_donation_date": self.last_donation_date,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    