from app.services.whatsappService import WhatsappService
from app.services.emailService import EmailService

class NotificationService:
    def __init__(self):
        self.whatsapp_service = WhatsappService()
        self.email_service = EmailService()
    
    async def send_whatsapp_otp(self, to_phone: str, template_name: str, params: dict):
        return await self.whatsapp_service.send_whatsapp_otp(to_phone, template_name, params)
    
    async def send_whatsapp_blood_alert(self, to_phone: str, blood_group: str, hospital: str):
        return await self.whatsapp_service.send_whatsapp_blood_alert(to_phone, blood_group, hospital)
    
    async def send_email_otp(self, to_email: str, template_name: str, params: dict):
        return await self.email_service.send_email_otp(to_email, template_name, params)
    
    async def send_email_blood_alert(self, to_email: str, blood_group: str, hospital: str):
        return await self.email_service.send_email_blood_alert(to_email, blood_group, hospital)
