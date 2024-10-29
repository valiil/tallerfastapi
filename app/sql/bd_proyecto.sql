-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-09-2024 a las 22:33:43
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributo`
--

CREATE TABLE `atributo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `atributo`
--

INSERT INTO `atributo` (`id`, `nombre`, `descripcion`) VALUES
(1, 'SOAT', 'Seguro Obligatorio de Accidentes de Tránsito'),
(2, 'Licencia', 'Tipo de licencia de conducción y número'),
(3, 'Tecno Mecánica', 'Certificado de revisión técnico-mecánica'),
(4, 'NIT', 'Número de Identificación Tributaria de la empresa'),
(5, 'Dirección', 'Dirección física del usuario o empresa'),
(6, 'Línea de Negocio', 'Descripción de la línea de negocio o actividad económica principal'),
(7, 'Tarjeta de Propiedad', 'Documento que acredita la propiedad del vehículo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributo_usuario`
--

CREATE TABLE `atributo_usuario` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_atributo` int(11) DEFAULT NULL,
  `valor` varchar(100) DEFAULT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `atributo_usuario`
--

INSERT INTO `atributo_usuario` (`id`, `id_usuario`, `id_atributo`, `valor`, `descripcion`) VALUES
(1, 1, 1, 'SOAT2024', 'SOAT vigente hasta 2024'),
(2, 2, 2, 'C123456', 'Licencia de conducción categoría C'),
(3, 3, 4, '900123456', 'NIT de la empresa logística'),
(4, 4, 3, 'Tecno2025', 'Revisión técnico-mecánica hasta 2025'),
(5, 5, 6, 'Transporte Internacional', 'Empresa global maneja transporte internacional'),
(11, 2, 7, 'TP2024', 'Tarjeta de propiedad vigente hasta 2024');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carga`
--

CREATE TABLE `carga` (
  `id` int(11) NOT NULL,
  `peso` decimal(10,2) DEFAULT NULL,
  `largo` decimal(10,2) DEFAULT NULL,
  `ancho` decimal(10,2) DEFAULT NULL,
  `alto` decimal(10,2) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_recogida` date DEFAULT NULL,
  `fecha_entrega` date DEFAULT NULL,
  `estado_actual` varchar(100) DEFAULT NULL,
  `origen` varchar(255) DEFAULT NULL,
  `destino` varchar(255) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `transportador` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carga`
--

INSERT INTO `carga` (`id`, `peso`, `largo`, `ancho`, `alto`, `descripcion`, `fecha_recogida`, `fecha_entrega`, `estado_actual`, `origen`, `destino`, `ubicacion`, `tipo`, `transportador`) VALUES
(1, 500.00, 2.00, 1.50, 1.00, 'Carga de alimentos', '2024-09-01', '2024-09-05', 'En tránsito', 'Bogotá', 'Medellín', 'Bodega 1', 'Alimentos', 'Juan\nMartínez'),
(2, 1000.00, 2.50, 2.00, 1.50, 'Carga de electrodomésticos', '2024-09-02', '2024-09-06', 'En tránsito', 'Cali', 'Barranquilla', 'Bodega 2', 'Electrodomésticos', 'Pedro\nRamírez'),
(3, 1500.00, 3.00, 2.50, 2.00, 'Carga de maquinaria', '2024-09-03', '2024-09-07', 'En tránsito', 'Medellín', 'Cartagena', 'Bodega 3', 'Maquinaria', 'Juan\nMartínez'),
(4, 750.00, 2.20, 1.80, 1.20, 'Carga de textiles', '2024-09-04', '2024-09-08', 'En tránsito', 'Bucaramanga', 'Santa Marta', 'Bodega 4', 'Textiles', 'Pedro\nRamírez'),
(5, 2000.00, 3.50, 2.00, 2.50, 'Carga de productos químicos', '2024-09-05', '2024-09-09', 'En tránsito', 'Cartagena', 'Cali', 'Bodega 5', 'Químicos', 'Pedro\nRamírez');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

CREATE TABLE `perfil` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `perfil`
--

INSERT INTO `perfil` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Administrador', 'Rol con todos los privilegios'),
(2, 'Transportador', 'Rol para módulos de transportador'),
(3, 'Empresa', 'Rol para módulos de empresa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transporte`
--

CREATE TABLE `transporte` (
  `matricula` varchar(50) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `color` varchar(30) DEFAULT NULL,
  `capacidad` int(11) DEFAULT NULL,
  `algo` varchar(100) DEFAULT NULL,
  `ancho` decimal(10,2) DEFAULT NULL,
  `largo` decimal(10,2) DEFAULT NULL,
  `año` year(4) DEFAULT NULL,
  `id_perfil` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `transporte`
--

INSERT INTO `transporte` (`matricula`, `modelo`, `tipo`, `color`, `capacidad`, `algo`, `ancho`, `largo`, `año`, `id_perfil`) VALUES
('ABC123', 'Freightliner Cascadia', 'Camión', 'Negro', 15000, 'Modelo 2022', 2.50, 7.00, '2022', 2),
('LMN789', 'Mercedes-Benz Actros', 'Camión', 'Rojo', 18000, 'Modelo 2023', 2.50, 7.20, '2023', 2),
('QWE147', 'Scania R 450', 'Camión', 'Azul', 17000, 'Modelo 2020', 2.40, 7.00, '2020', 2),
('RTY258', 'MAN TGX', 'Camión', 'Gris', 16000, 'Modelo 2022', 2.50, 7.10, '2022', 2),
('XYZ456', 'Volvo FH', 'Camión', 'Blanco', 20000, 'Modelo 2021', 2.60, 7.50, '2021', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(150) NOT NULL,
  `documento` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `id_perfil` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `contrasena`, `nombre`, `apellidos`, `documento`, `telefono`, `id_perfil`) VALUES
(1, 'admin_master', 'Admin2024!', 'Juan', 'Martínez', '1023456789', '+573001234567', 1),
(2, 'transp_jorge', 'TranspJor21$', 'Jorge', 'Hernández', '1011234567', '+573002345678', 2),
(3, 'empresa_logistics', 'EmpLog2024#', 'Lucía', 'González', '900123456', '+573003456789', 3),
(4, 'transp_pedro', 'PedroTrans@2024', 'Pedro', 'Ramírez', '1012233445', '+573004567890', 2),
(5, 'empresa_global', 'Global123$', 'Marta', 'Rodríguez', '900234567', '+573005678901', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `atributo_usuario`
--
ALTER TABLE `atributo_usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_atributo` (`id_atributo`);

--
-- Indices de la tabla `carga`
--
ALTER TABLE `carga`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `transporte`
--
ALTER TABLE `transporte`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `id_perfil` (`id_perfil`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_perfil` (`id_perfil`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `atributo`
--
ALTER TABLE `atributo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `atributo_usuario`
--
ALTER TABLE `atributo_usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `carga`
--
ALTER TABLE `carga`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `perfil`
--
ALTER TABLE `perfil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `atributo_usuario`
--
ALTER TABLE `atributo_usuario`
  ADD CONSTRAINT `atributo_usuario_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `atributo_usuario_ibfk_2` FOREIGN KEY (`id_atributo`) REFERENCES `atributo` (`id`);

--
-- Filtros para la tabla `transporte`
--
ALTER TABLE `transporte`
  ADD CONSTRAINT `transporte_ibfk_1` FOREIGN KEY (`id_perfil`) REFERENCES `perfil` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_perfil`) REFERENCES `perfil` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
