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


settings = Settings()
