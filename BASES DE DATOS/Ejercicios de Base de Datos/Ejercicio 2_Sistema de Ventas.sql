-- Crear base de datos
CREATE DATABASE IF NOT EXISTS ventas;
USE ventas;

-- Tabla clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100)
);

-- Tabla productos
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL
);

-- Tabla facturas
CREATE TABLE facturas (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT NOT NULL,
    fecha DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Insertar clientes
INSERT INTO clientes (nombre, correo) VALUES
('Dennis Montero', 'dmontero@gmail.com'),
('Carlos Garcia', 'cgarcia@gmail.com');

-- Insertar productos
INSERT INTO productos (nombre, precio) VALUES
('Memoria USB 64GB', 486.28),
('Mouse', 100.00),
('Teclado', 250.00);

-- Insertar facturas
INSERT INTO facturas (id_cliente, id_producto, cantidad, fecha) VALUES
(1, 1, 1, '2025-01-10'),
(1, 2, 2, '2025-01-11'),
(2, 3, 1, '2025-01-15');

-- Consultas

-- 1. Mostrar facturas con nombre del cliente y producto
SELECT f.id_factura, c.nombre AS cliente, p.nombre AS producto, f.cantidad, f.fecha
FROM facturas f
JOIN clientes c ON f.id_cliente = c.id_cliente
JOIN productos p ON f.id_producto = p.id_producto;

-- 2. Total gastado por un cliente
SELECT c.nombre, SUM(p.precio * f.cantidad) AS total_gastado
FROM facturas f
JOIN clientes c ON f.id_cliente = c.id_cliente
JOIN productos p ON f.id_producto = p.id_producto
WHERE c.id_cliente = 1
GROUP BY c.id_cliente;

-- 3. Mostrar todos los clientes
SELECT * FROM clientes;

-- 4. Mostrar todos los productos
SELECT * FROM productos;

-- 5. Mostrar todos las facturas
SELECT * FROM facturas;