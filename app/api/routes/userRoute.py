from fastapi import APIRouter
from app.api.controllers.userController import UserController


router = APIRouter()
user_controller = UserController()

@router.post("/users")
async def create_user(data:dict):
    return await user_controller.create_user_service(data)