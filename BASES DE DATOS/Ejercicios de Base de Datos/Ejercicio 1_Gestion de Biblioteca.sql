-- Crear base de datos
CREATE DATABASE IF NOT EXISTS biblioteca;
USE biblioteca;

-- Tabla autores
CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);

-- Tabla libros
CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    genero VARCHAR(50),
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);

-- Insertar autores
INSERT INTO autores (nombre, nacionalidad) VALUES
('Gabriel Garcia Marquez', 'Colombiana'),
('Julio Verne', 'Francesa'),
('Isabel Allende', 'Chilena'),
('Mario Vargas Llosa', 'Peruana'),
('George Orwell', 'Britanica'),
('Jane Austen', 'Britanica');

-- Insertar libros
INSERT INTO libros (titulo, genero, id_autor) VALUES
('El amor en los tiempos del colera', 'Novela', 1),
('Viaje al centro de la Tierra', 'Ciencia ficcion', 2),
('La casa de los espiritus', 'Novela', 3),
('Conversacion en la catedral', 'Novela', 4),
('1984', 'Distopia', 5),
('Orgullo y prejuicio', 'Romance', 6);

-- Consultas

-- 1. Mostrar todos los libros
SELECT * FROM libros;

-- 2. Mostrar todos los autores
SELECT * FROM autores;

-- 3. Mostrar todos los libros con su autor
SELECT l.titulo, a.nombre AS autor
FROM libros l
JOIN autores a ON l.id_autor = a.id_autor;

-- 4. Listar libros de un genero especifico
SELECT titulo FROM libros WHERE genero = 'Novela';