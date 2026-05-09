from fastapi import APIRouter, Request
from app.services.webhookService import email_reply

router = APIRouter()

@router.post("/webhooks/email-reply")
async def email_reply_endpoint(request: Request):
    return await email_reply(request)
