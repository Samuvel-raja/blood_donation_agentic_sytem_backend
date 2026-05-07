import httpx
from config import settings
from core.exceptions import NotificationProvider
from app.services.templates import render_whatsapp_params

class WhatsappService:
    def __init__(self):
        self.whatsapp_phone_number_id = settings.whatsapp_phone_number_id
        self.whatsapp_token = settings.whatsapp_token
        self.whatsapp_base_url = settings.whatsapp_uri


    async def __send(self,payload:dict):
        url = f"{self.whatsapp_base_url}/{self.whatsapp_phone_number_id}/messages"
        headers = {
            "Authorization": f"Bearer {self.whatsapp_token}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)

            if response.status_code != 200:
                raise NotificationProvider(f"Whatsapp api Failed to send message: {response.text}")
            
            return response.json()
    
    async def send_whatsapp_otp(self, to_phone:str, template_name:str, params:dict):
        params = render_whatsapp_params(template_name, params)

        payload = {
            "messaging_product": "whatsapp",
            "to": to_phone,  
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": "en"},
                "components": [{"type": "body", "parameters": params}]
            }
        }
        res = await self._send(payload)
        return res
    
    async def send_whatsapp_blood_alert(self, to_phone:str, blood_group:str, hospital:str):
        params = render_whatsapp_params(
            "blood_alert",
            {"blood_group": blood_group, "hospital": hospital}
        )

        payload = {
            "messaging_product": "whatsapp",
            "to": to_phone,
            "type": "template",
            "template": {
                "name": "blood_alert",
                "language": {"code": "en"},
                "components": [{"type": "body", "parameters": params}]
            }
        }
        res = await self._send(payload)
        return res
