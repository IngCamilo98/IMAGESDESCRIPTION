CREATE DATABASE IF NOT EXISTS DescriptionImages;
USE DescriptionImages;
CREATE TABLE IF NOT EXISTS images(
    id_imagen INTEGER PRIMARY KEY NOT NULL,
    ruta_local TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    updated_at timestamp not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);