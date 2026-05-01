from fastapi import FastAPI
import uvicorn
from config import settings
from logging import getLogger

logger = getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    logger.info(f"OpenAI API Key: {settings.openai_api_key}")
    return {"Hello": settings.openai_api_key}


if __name__ == "__main__":
    logger.info(f"OpenAI API Key: {settings.openai_api_key}")
    logger.info(f"Gemini API Key: {settings.gemini_api_key}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
