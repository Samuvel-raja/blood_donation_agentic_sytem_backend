import aiosmtplib
from config import settings
from email.message import EmailMessage
from app.services.templates import render_email

class EmailService:
    def __init__(self):
        self.smtp_host = settings.smtp_host
        self.smtp_port = settings.smtp_port
        self.email_user = settings.email_user
        self.email_password = settings.email_pass
    
    async def send_email_otp(self,to_email:str,subject:str,otp:str):
        content = render_email("otp", {"otp": otp})
        await self.send_email(to_email, subject, content)

    async def send_email_blood_alert(self,to_email:str,blood_group:str,hospital:str,subject:str):
        content = render_email("blood_alert", {"blood_group": blood_group, "hospital": hospital})
        await self.send_email(to_email, subject, content)
    
    async def send_email(self, to_email:str,subject:str,content:str):
        msg = EmailMessage()
        msg['From']=self.email_user
        msg['To']=to_email
        msg["Subject"]=subject
        msg.set_content(content)

        await aiosmtplib.send(
            msg,
            hostname=self.smtp_host,
            port=self.smtp_port,
            username=self.email_user,
            password=self.email_password,
            use_tls=True
        )