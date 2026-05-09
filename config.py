from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
        env_ignore_empty=True,
    )
    openai_api_key: str
    gemini_api_key: str
    mongo_uri: str
    mongo_db: str
    whatsapp_token: str
    whatsapp_phone_number_id: str
    whatsapp_uri: str
    email_user: str
    email_pass: str
    smtp_host: str
    smtp_port: int
    resend_api_key: str
    mailgun_api_key: str
    mailgun_domain: str
    mailgun_base_url: str
    google_maps_api_key: str
    google_maps_places_url: str


settings = Settings()
