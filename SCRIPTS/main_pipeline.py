print('Hello world')
print('Hello world')
"""

# 1. Configuración inicial y carga de credenciales
FUNCION: cargar_variables_de_entorno()
    - Carga GOOGLE_API_KEY, credenciales de MySQL (host, user, pass) desde CONFIG/.env
    - Si falla, imprime error y termina el programa.

FUNCION: configurar_api_gemini(api_key)
    - Inicializa la librería de Gemini con la clave API.
    - Si falla, imprime error y termina el programa.

# 2. Configuración de la base de datos (una vez al inicio del pipeline o si no existe la tabla)
FUNCION: asegurar_tabla_mysql()
    - CONECTAR a MySQL (usando credenciales del .env).
    - VERIFICAR si la tabla 'image_descriptions' existe.
    - SI NO EXISTE:
        - CREAR la tabla 'image_descriptions' con columnas para:
            - id (clave primaria, auto-incremento)
            - image_path (TEXTO, para la ruta del archivo)
            - description (TEXTO LARGO, para la descripción de Gemini)
            - created_at (TIMESTAMP, para la fecha de carga)
    - DESCONECTAR de MySQL.
    - Si falla, imprime error y termina el programa.


# --- Inicio del Proceso Principal del Pipeline ---

# Llamar a las funciones de configuración
llamar cargar_variables_de_entorno()
llamar configurar_api_gemini(GOOGLE_API_KEY)
llamar asegurar_tabla_mysql()


# 3. Etapa de Extracción (Extract) - Recorrer imágenes
FUNCION: obtener_rutas_imagenes(carpeta_imagenes)
    - INPUT: Ruta a la carpeta DATA/ (ej. `/home/sircamilot/Documents/ImagesDescription/DATA/`)
    - RECORRER recursivamente todos los archivos en `carpeta_imagenes`.
    - FILTRAR solo los archivos que sean imágenes (ej. `.jpg`, `.png`, `.jpeg`).
    - DEVOLVER una lista de rutas completas de imágenes encontradas.
    - Si no encuentra imágenes o la carpeta no existe, imprime advertencia/error.

# Llamar a la función de extracción
rutas_de_imagenes = obtener_rutas_imagenes(PROJECT_ROOT / "DATA/")


# 4. Etapa de Transformación (Transform) - Generar descripciones con Gemini
FUNCION: generar_descripciones_gemini(lista_rutas_imagenes)
    - INPUT: La lista de rutas de imágenes de la etapa anterior.
    - PARA CADA `ruta_imagen` en `lista_rutas_imagenes`:
        - INTENTAR:
            - CARGAR la imagen desde `ruta_imagen`.
            - LLAMAR al modelo Gemini (`gemini-1.5-flash`) con un prompt y la imagen.
            - OBTENER la `descripcion` de la respuesta de Gemini.
            - ALMACENAR la `ruta_imagen` y su `descripcion` en una lista temporal de resultados.
        - EXCEPTO si hay un ERROR (ej. API falla, imagen corrupta):
            - REGISTRAR el error para esa `ruta_imagen` (ej. en un log o en la consola).
            - Continuar con la siguiente imagen (no detener todo el proceso).
    - DEVOLVER la lista temporal de `{ruta_imagen, descripcion}` (solo las que se procesaron con éxito).

# Llamar a la función de transformación
descripciones_listas_para_cargar = generar_descripciones_gemini(rutas_de_imagenes)


# 5. Etapa de Carga (Load) - Insertar en MySQL
FUNCION: cargar_a_mysql(datos_a_cargar, credenciales_mysql)
    - INPUT: La lista de `{ruta_imagen, descripcion}` de la etapa anterior.
    - CONECTAR a MySQL (usando credenciales del .env).
    - PARA CADA `item` en `datos_a_cargar`:
        - INTENTAR:
            - PREPARAR una sentencia SQL INSERT para la tabla `image_descriptions`.
            - INSERTAR `item.ruta_imagen` y `item.descripcion` en la tabla.
            - REGISTRAR que la inserción fue exitosa.
        - EXCEPTO si hay un ERROR (ej. conexión a DB falla, error SQL):
            - REGISTRAR el error para ese `item` (en un log o consola).
            - Continuar con el siguiente item.
    - DESCONECTAR de MySQL.
    - Si la conexión inicial a MySQL falla, imprime error y termina el programa.

# Llamar a la función de carga
cargar_a_mysql(descripciones_listas_para_cargar, MYSQL_CREDENTIALS)


# --- Finalización del Pipeline ---
IMPRIMIR mensaje de éxito o resumen de errores. 
Esot solo lo es para sumar algo

"""
