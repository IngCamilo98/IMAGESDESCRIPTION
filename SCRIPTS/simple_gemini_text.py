import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai # La forma correcta de importar la librería de Gemini

print("--- Iniciando la aplicación Gemini Simple ---")

# --- 1. Cargar la clave de API desde el archivo .env ---
# Calculamos la ruta a la raíz del proyecto para encontrar la carpeta CONFIG
# __file__ es SCRIPTS/simple_gemini_text.py
# .parent es SCRIPTS/
# .parent.parent es ImagesDescription/ (la raíz del proyecto)
project_root = Path(__file__).parent.parent
dotenv_path = project_root / "CONFIG" / ".env"

print(f"Intentando cargar .env desde: {dotenv_path}")

try:
    load_dotenv(dotenv_path)
    print(".env cargado con éxito.")
except Exception as e:
    print(f"ERROR: No se pudo cargar el archivo .env. Detalles: {e}")
    print(f"Por favor, asegúrate de que '{dotenv_path}' exista y sea accesible.")
    exit(1) # Salir si el .env no carga

# Obtener la clave de API de la variable de entorno GOOGLE_API_KEY
gemini_api_key = os.getenv("GOOGLE_API_KEY")

if not gemini_api_key:
    print("ERROR: La clave de API 'GOOGLE_API_KEY' no se encontró en el archivo .env.")
    print("Asegúrate de que tu .env tenga GOOGLE_API_KEY=\"TU_CLAVE_REAL\".")
    exit(1) # Salir si la clave no está

# --- 2. Configurar la librería de Gemini con tu clave de API ---
try:
    genai.configure(api_key=gemini_api_key)
    print("Librería Gemini configurada con la clave de API.")
except Exception as e:
    print(f"ERROR: No se pudo configurar la librería Gemini. Detalles: {e}")
    print("Verifica si tu clave de API es válida o si hay un problema de conexión.")
    exit(1) # Salir si la configuración falla

# --- 3. Seleccionar el modelo de Gemini ---
# Usaremos el modelo 'gemini-1.5-flash' que es rápido y económico para texto.
# También puedes usar 'gemini-1.5-pro' para mayor capacidad, pero puede tener un costo.
model = genai.GenerativeModel("gemini-1.5-flash")
print("Modelo 'gemini-1.5-flash' seleccionado.")

# --- 4. Enviar una pregunta y obtener una respuesta ---
question = "¿Cómo es el nombre de chespirito?"
print(f"\nEnviando pregunta a Gemini: \"{question}\"")

try:
    response = model.generate_content(question)
    print("\n--- Respuesta de Gemini ---")
    print(response.text)
    print("---------------------------\n")
except Exception as e:
    print(f"ERROR: No se pudo obtener respuesta de Gemini. Detalles: {e}")
    print("Posibles razones: Problemas de conexión, clave de API inválida, o cuotas excedidas.")
    exit(1) # Salir si la solicitud falla

print("--- Ejecución del programa finalizada ---")