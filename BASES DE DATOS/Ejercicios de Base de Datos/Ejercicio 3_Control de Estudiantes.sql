-- Crear base de datos
CREATE DATABASE IF NOT EXISTS colegio;
USE colegio;

-- Tabla estudiantes
CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE
);

-- Tabla cursos
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Tabla matriculas
CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    fecha_matricula DATE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

-- Insertar datos
INSERT INTO estudiantes (nombre, fecha_nacimiento) VALUES
('Dennis Montero', '2008-03-15'),
('Carlos Garcia', '2007-11-02');

INSERT INTO cursos (nombre) VALUES
('Matematicas'),
('Historia'),
('Biologia');

INSERT INTO matriculas (id_estudiante, id_curso, fecha_matricula) VALUES
(1, 1, '2025-02-01'),
(1, 2, '2025-02-02'),
(2, 3, '2025-02-03');

-- Consultas

-- 1. Mostrar todos los estudiantes
SELECT * FROM estudiantes;

-- 2. Monstrar todos los cursos
SELECT * FROM cursos;

-- 3. Mostrar todos las matriculas
SELECT * FROM matriculas;

-- 4. Mostrar cursos matriculados por estudiante
SELECT e.nombre AS estudiante, 
       c.nombre AS curso, 
       m.fecha_matricula
FROM matriculas m
JOIN estudiantes e ON m.id_estudiante = e.id_estudiante
JOIN cursos c ON m.id_curso = c.id_curso;

-- 5. Contar cuantas materias tiene cada estudiante
SELECT e.nombre, COUNT(m.id_curso) AS cantidad_cursos
FROM matriculas m
JOIN estudiantes e ON m.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante;