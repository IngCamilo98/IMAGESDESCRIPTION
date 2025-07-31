import mysql.connector
from pathlib import Path
from dotenv import load_dotenv
import os

project_root = Path(__file__).parent.parent
dotenv_path = project_root / "CONFIG" / ".env"

try:
    load_dotenv(dotenv_path)
    print(".env cargado con éxito.")
except Exception as e:
    print(f"ERROR: No se pudo cargar el archivo .env. Detalles: {e}")
    print(f"Asegúrate de que '{dotenv_path}' exista y sea accesible.")
    exit(1)

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
database = os.getenv("BD")

# Establecer la conexión
conexion = mysql.connector.connect(
    host=f'{host}',        # o "127.0.0.1"
    user=f'{user}',       # por ejemplo: "root"
    password=f'{password}',
    database=f'{database}' # opcional si aún no te conectas a una base
)

# Crear cursor
cursor = conexion.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM images;")

# Obtener resultados
resultados = cursor.fetchall()

# Mostrar resultados
for fila in resultados:
    print(fila)

# Cerrar cursor y conexión
cursor.close()
conexion.close()
