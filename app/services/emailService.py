from config import settings
from app.tools.templateTool import render_email
from app.tools.mailgunTool import mailgun_send_email

class EmailService:
    def __init__(self):
        self.mailgun_api_key = settings.mailgun_api_key
        self.mailgun_domain = settings.mailgun_domain
        self.mailgun_base_url = settings.mailgun_base_url

    async def send_email_otp(self, to_email: str, otp: str):
        content = render_email("otp", {"otp": otp})
        await self.send_email(to_email, content["subject"], content["html"])


    async def send_email_blood_alert(self, to_email: str, blood_group: str, hospital: str):
        content = render_email("blood_alert", {"blood_group": blood_group, "hospital": hospital})
        await self.send_email(to_email, content["subject"], content["html"])


    async def send_email(self, to_email: str, subject: str, html: str):
        return await mailgun_send_email(to_email, subject, html)
