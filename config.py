from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
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


settings = Settings()
