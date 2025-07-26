import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar .env desde carpeta config/
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

# Acceder a variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
