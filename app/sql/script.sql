-- Crear la base de datos
CREATE DATABASE bd_proyecto;

-- Usar la base de datos
USE bd_proyecto;

-- Tabla Perfil
CREATE TABLE perfil (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla Usuario
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100) NOT NULL,
    contrasena VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    documento VARCHAR(50),
    telefono VARCHAR(20),
    id_perfil INT,
    FOREIGN KEY (id_perfil) REFERENCES perfil(id)
);

-- Tabla Atributo
CREATE TABLE atributo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla Atributo_Usuario
CREATE TABLE atributo_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_atributo INT,
    valor VARCHAR(100),
    descripcion TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_atributo) REFERENCES atributo(id)
);

-- Tabla Transporte
CREATE TABLE transporte (
    matricula VARCHAR(50) PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    color VARCHAR(30),
    capacidad INT,
    algo VARCHAR(100),
    ancho DECIMAL(10, 2),
    largo DECIMAL(10, 2),
    año YEAR,
    id_perfil INT,
    FOREIGN KEY (id_perfil) REFERENCES perfil(id)
);

-- Tabla Carga
CREATE TABLE carga (
    id INT AUTO_INCREMENT PRIMARY KEY,
    peso DECIMAL(10, 2),
    largo DECIMAL(10, 2),
    ancho DECIMAL(10, 2),
    alto DECIMAL(10, 2),
    descripcion TEXT,
    fecha_recogida DATE,
    fecha_entrega DATE,
    estado_actual VARCHAR(100),
    origen VARCHAR(255),
    destino VARCHAR(255),
    ubicacion VARCHAR(255),
    tipo VARCHAR(100),
    id_perfil INT,
    FOREIGN KEY (id_perfil) REFERENCES perfil(id)
);