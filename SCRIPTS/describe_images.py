import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

print("--- Iniciando la aplicación Gemini para descripción de imágenes ---")

# --- 1. Cargar la clave de API desde el archivo .env ---
project_root = Path(__file__).parent.parent
dotenv_path = project_root / "CONFIG" / ".env"

try:
    load_dotenv(dotenv_path)
    print(".env cargado con éxito.")
except Exception as e:
    print(f"ERROR: No se pudo cargar el archivo .env. Detalles: {e}")
    print(f"Asegúrate de que '{dotenv_path}' exista y sea accesible.")
    exit(1)

gemini_api_key = os.getenv("GOOGLE_API_KEY")

if not gemini_api_key:
    print("ERROR: La clave de API 'GOOGLE_API_KEY' no se encontró en el archivo .env.")
    print("Asegúrate de que tu .env tenga GOOGLE_API_KEY=\"TU_CLAVE_REAL\".")
    exit(1)

# --- 2. Configurar la librería de Gemini con tu clave de API ---
try:
    genai.configure(api_key=gemini_api_key)
    print("Librería Gemini configurada con la clave de API.")
except Exception as e:
    print(f"ERROR: No se pudo configurar la librería Gemini. Detalles: {e}")
    exit(1)

# --- 3. Seleccionar el modelo de Gemini Vision ---
model = genai.GenerativeModel("gemini-1.5-flash")
print("Modelo 'gemini-1.5-flash' seleccionado.")

# --- 4. Definir la ruta a la imagen ---
# ¡CAMBIA ESTA RUTA A LA DE TU IMAGEN DE PRUEBA!
image_path = project_root / "DATA" / "IMAGES" /"IMG-0001.jpg"
print(f"Intentando abrir la imagen desde: {image_path}")

try:
    img = Image.open(image_path)
    print("Imagen abierta con éxito.")
except FileNotFoundError:
    print(f"ERROR: No se encontró la imagen en la ruta: {image_path}")
    exit(1)
except Exception as e:
    print(f"ERROR: No se pudo abrir la imagen. Detalles: {e}")
    exit(1)

# --- 5. Crear el contenido para la solicitud (texto + imagen) ---
prompt = "Describe detalladamente el contenido de esta imagen."
contents = [prompt, img]

print("\nEnviando solicitud de descripción de imagen a Gemini...")

# --- 6. Enviar la solicitud y obtener la respuesta ---
try:
    response = model.generate_content(contents)
    print("\n--- Descripción de la imagen por Gemini ---")
    print(response.text)
    print("-----------------------------------------\n")
except Exception as e:
    print(f"ERROR: No se pudo obtener la descripción de la imagen. Detalles: {e}")
    print("Posibles razones: Problemas de conexión, clave de API inválida, formato de imagen no compatible.")
    exit(1)

print("--- Ejecución del programa finalizada ---")