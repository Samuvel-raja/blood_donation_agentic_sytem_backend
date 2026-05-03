from app.services.userService import create_user
class UserController:
    async def create_user_service(self,data):
        user = create_user(data)
        return {
            "id": str(user.id),
            "name": user.name,
            "email": user.email,
            "mobile": user.mobile,
            "blood_group": user.blood_group
        }