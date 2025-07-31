CREATE DATABASE IF NOT EXISTS DescriptionImages;
USE DescriptionImages;
CREATE TABLE IF NOT EXISTS images(
    id_imagen INTEGER PRIMARY KEY NOT NULL,
    ruta_local TEXT NOT NULL,
    descript TEXT NOT NULL,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    updated_at timestamp not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);

INSERT INTO images (id_imagen, ruta_local, descript) VALUES
(1, '/imagenes/foto1.jpg', 'Foto de un paisaje al atardecer'),
(2, '/imagenes/foto2.jpg', 'Retrato en blanco y negro'),
(3, '/imagenes/foto3.jpg', 'Imagen promocional de producto'),
(4, '/imagenes/foto4.jpg', 'Logo de la empresa actualizado'),
(5, '/imagenes/foto5.jpg', 'Captura de pantalla de la aplicación');


