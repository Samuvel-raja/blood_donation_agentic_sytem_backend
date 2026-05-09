from fastapi import FastAPI
import uvicorn
from config import settings
from app.api.routes.userRoute import router as user_router
from app.api.routes.bloodRequestRoute import router as blood_request_router
from app.api.routes.webhookRoute import router as webhook_router
from app.core.exception_handler import global_exception_handler
from app.database.models.connection import init_db
import app.core.logging

app = FastAPI()

init_db()

app.include_router(user_router)
app.include_router(blood_request_router)
app.include_router(webhook_router)
app.add_exception_handler(Exception, global_exception_handler)


if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)
