Idea general del proyecto 
[Carpeta DATA/IMAGES]
       |
       v
[Script Python] -> Recorrer imágenes
       |
       v
[Lista de Rutas de Imágenes]
       |
       v
[Script Python] -> Llamar a la API de Gemini para cada imagen
       |
       v
[Lista de {ruta, descripción}]
       |
       v
[Script Python] -> Conectar a MySQL e insertar
       |
       v
[Tabla `image_descriptions` en MySQL]

Conexion con Mysql
pip install mysql-connector-python

