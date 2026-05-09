
import httpx
from config import settings

async def mailgun_send_email(to_email: str, subject: str, html: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.mailgun_base_url}/v3/{settings.mailgun_domain}/messages",
            auth=("api", settings.mailgun_api_key),
            data={
                "from":(
                        "PulseXira "
                            f"<postmaster@{settings.mailgun_domain}>"
                        ),
                "to":[to_email],
                "subject":subject,
                "html":html,
                "h:Reply-To":(
                            "reply@"
                            f"{settings.mailgun_domain}"
                        )
                }
            )

        return response.json()