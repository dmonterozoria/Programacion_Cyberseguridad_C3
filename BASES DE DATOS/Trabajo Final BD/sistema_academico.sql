-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS sistema_academico;
USE sistema_academico;

-- Tabla de departamentos
CREATE TABLE departamento (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de estudiantes
CREATE TABLE estudiante (
    id_estudiante INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    id_departamento INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

-- Tabla de profesores
CREATE TABLE profesor (
    id_profesor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    id_departamento INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

-- Tabla de cursos
CREATE TABLE curso (
    id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    creditos INT NOT NULL CHECK (creditos BETWEEN 1 AND 6),
    id_departamento INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

-- Tabla de clases
CREATE TABLE clase (
    id_clase INT PRIMARY KEY AUTO_INCREMENT,
    id_curso INT NOT NULL,
    id_profesor INT NOT NULL,
    ano INT NOT NULL,
    semestre VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
    FOREIGN KEY (id_profesor) REFERENCES profesor(id_profesor),
    UNIQUE KEY (id_curso, id_profesor, año, semestre)
);

-- Tabla de inscripciones
CREATE TABLE inscripcion (
    id_inscripcion INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT NOT NULL,
    id_clase INT NOT NULL,
    fecha_inscripcion DATE NOT NULL DEFAULT (CURRENT_DATE),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_clase) REFERENCES clase(id_clase),
    UNIQUE KEY (id_estudiante, id_clase) -- Evita inscripciones duplicadas
);

-- Tabla de calificaciones
CREATE TABLE Calificacion (
    id_calificacion INT PRIMARY KEY AUTO_INCREMENT,
    id_inscripcion INT NOT NULL,
    nota DECIMAL(4,2) NOT NULL CHECK (nota BETWEEN 0 AND 100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_inscripcion) REFERENCES inscripcion(id_inscripcion)
);

-- Insertar Departamentos
INSERT INTO departamento (nombre) VALUES ('Ingenieria');
INSERT INTO departamento (nombre) VALUES ('Matematicas');
INSERT INTO departamento (nombre) VALUES ('Historia');
INSERT INTO departamento (nombre) VALUES ('Biologia');
INSERT INTO departamento (nombre) VALUES ('Filosofia');
INSERT INTO departamento (nombre) VALUES ('Economia');

-- Insertar Estudiantes
INSERT INTO estudiante (nombre, apellido, fecha_nacimiento, email, id_departamento) VALUES
('Carlos', 'Ruiz', '2000-05-12', 'carlos.ruiz@email.com', 1),
('Ana', 'Martinez', '1999-08-20', 'ana.martinez@email.com', 2),
('Luis', 'Fernandez', '2001-01-15', 'luis.fernandez@email.com', 1),
('Maria', 'Lopez', '2000-11-30', 'maria.lopez@email.com', 3),
('Jose', 'Ramirez', '2002-03-10', 'jose.ramirez@email.com', 4),
('Laura', 'Castro', '1998-07-25', 'laura.castro@email.com', 5),
('Miguel', 'Torres', '2001-09-18', 'miguel.torres@email.com', 6),
('Sofia', 'Diaz', '2000-02-22', 'sofia.diaz@email.com', 2);

-- Insertar Profesores
INSERT INTO profesor (nombre, apellido, email, id_departamento) VALUES
('Juan', 'Perez', 'juan.perez@uni.edu', 1),
('Marta', 'Gomez', 'marta.gomez@uni.edu', 2),
('Pedro', 'Santos', 'pedro.santos@uni.edu', 3),
('Laura', 'Ramirez', 'laura.ramirez@uni.edu', 4),
('Andres', 'Morales', 'andres.morales@uni.edu', 5),
('Claudia', 'Vega', 'claudia.vega@uni.edu', 6);

-- Insertar Cursos
INSERT INTO curso (nombre, creditos, id_departamento) VALUES ('Curso Minus 1', 4, 1);
INSERT INTO curso (nombre, creditos, id_departamento) VALUES ('Curso Voluptas 2', 3, 2);
INSERT INTO curso (nombre, creditos, id_departamento) VALUES ('Curso Qui 3', 2, 3);
INSERT INTO curso (nombre, creditos, id_departamento) VALUES ('Curso Omnis 4', 5,4);
INSERT INTO curso (nombre, creditos, id_departamento) VALUES ('Curso Cum 5', 4, 5);
INSERT INTO curso (nombre, creditos, id_departamento) VALUES ('Curso Harum 6', 3, 6);

-- Insertar Clases
INSERT INTO clase (id_curso, id_profesor, año, semestre) VALUES
(1, 1, 2025, 'Primavera'),
(2, 2, 2025, 'Otono'),
(3, 3, 2025, 'Primavera'),
(4, 4, 2025, 'Otono'),
(5, 5, 2025, 'Primavera'),
(6, 6, 2025, 'Otono');

-- Insertar Inscripciones
INSERT INTO inscripcion (id_estudiante, id_clase, fecha_inscripcion) VALUES
(1, 1, '2025-02-01'),
(2, 2, '2025-02-02'),
(3, 1, '2025-02-03'),
(4, 3, '2025-02-04'),
(5, 4, '2025-02-05'),
(6, 5, '2025-02-06'),
(7, 6, '2025-02-07'),
(8, 2, '2025-02-08');

-- Insertar Calificiones
INSERT INTO calificacion (id_inscripcion, nota) VALUES
(1, 95.50),
(2, 88.00),
(3, 76.25),
(4, 90.00),
(5, 82.75),
(6, 91.00),
(7, 85.50),
(8, 78.25);

-- CONSULTA BASICA: LISTAR ESTUDIANTES
SELECT * FROM estudiante;

-- CONSULTA BASICA: LISTAR CURSOS
SELECT * FROM curso;

-- JOIN: ESTUDIANTES INSCRITOS POR CURSO
SELECT e.nombre AS estudiante, c.nombre AS curso
FROM inscripcion i
JOIN estudiante e ON i.id_estudiante = e.id_estudiante
JOIN clase cl ON i.id_clase = cl.id_clase
JOIN curso c ON cl.id_curso = c.id_curso;

-- JOIN: CURSOS IMPARTIDOS POR CADA PROFESOR

SELECT p.nombre, p.apellido, COUNT(DISTINCT c.id_clase) AS total_clases
FROM profesor p
JOIN clase c ON p.id_profesor = c.id_profesor
GROUP BY p.id_profesor;

-- JOIN: ESTUDIANTES Y SUS CALIFICACIONES
SELECT e.nombre, c.nota
FROM calificacion c
JOIN inscripcion i ON c.id_inscripcion = i.id_inscripcion
JOIN estudiante e ON i.id_estudiante = e.id_estudiante;

-- ESTADISTICA: PROMEDIO DE CALIFICACIONES POR CURSO
SELECT cu.nombre AS curso, AVG(ca.nota) AS promedio
FROM calificacion ca
JOIN inscripcion i ON ca.id_inscripcion = i.id_inscripcion
JOIN clase cl ON i.id_clase = cl.id_clase
JOIN curso cu ON cl.id_curso = cu.id_curso
GROUP BY cu.id_curso;

-- ESTADISTICA: NUMERO DE ESTUDIANTES POR CURSO
SELECT cu.nombre, COUNT(i.id_inscripcion) AS inscritos
FROM inscripcion i
JOIN clase cl ON i.id_clase = cl.id_clase
JOIN curso cu ON cl.id_curso = cu.id_curso
GROUP BY cu.id_curso;

-- ACTUALIZAR NOMBRE DE CURSO
UPDATE curso
SET nombre = 'Curso Mollitia 18'
WHERE id_curso = 1;

-- ELIMINAR UNA CALIFICACION
DELETE FROM calificacion 
WHERE id_calificacion = 1;
