import os
from dotenv import load_dotenv

load_dotenv()

SERVER_PORT = os.getenv("SERVER_PORT", 3001)
MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")