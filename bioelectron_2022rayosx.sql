-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-10-2022 a las 15:20:07
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bioelectron#2022rayosx`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add blacklisted token', 6, 'add_blacklistedtoken'),
(22, 'Can change blacklisted token', 6, 'change_blacklistedtoken'),
(23, 'Can delete blacklisted token', 6, 'delete_blacklistedtoken'),
(24, 'Can view blacklisted token', 6, 'view_blacklistedtoken'),
(25, 'Can add outstanding token', 7, 'add_outstandingtoken'),
(26, 'Can change outstanding token', 7, 'change_outstandingtoken'),
(27, 'Can delete outstanding token', 7, 'delete_outstandingtoken'),
(28, 'Can view outstanding token', 7, 'view_outstandingtoken'),
(29, 'Can add Usuario', 8, 'add_user'),
(30, 'Can change Usuario', 8, 'change_user'),
(31, 'Can delete Usuario', 8, 'delete_user'),
(32, 'Can view Usuario', 8, 'view_user'),
(33, 'Can add historical Usuario', 9, 'add_historicaluser'),
(34, 'Can change historical Usuario', 9, 'change_historicaluser'),
(35, 'Can delete historical Usuario', 9, 'delete_historicaluser'),
(36, 'Can view historical Usuario', 9, 'view_historicaluser'),
(37, 'Can add ar_dpt_ model', 10, 'add_ar_dpt_model'),
(38, 'Can change ar_dpt_ model', 10, 'change_ar_dpt_model'),
(39, 'Can delete ar_dpt_ model', 10, 'delete_ar_dpt_model'),
(40, 'Can view ar_dpt_ model', 10, 'view_ar_dpt_model'),
(41, 'Can add areas model', 11, 'add_areasmodel'),
(42, 'Can change areas model', 11, 'change_areasmodel'),
(43, 'Can delete areas model', 11, 'delete_areasmodel'),
(44, 'Can view areas model', 11, 'view_areasmodel'),
(45, 'Can add con_ dpt_ model', 12, 'add_con_dpt_model'),
(46, 'Can change con_ dpt_ model', 12, 'change_con_dpt_model'),
(47, 'Can delete con_ dpt_ model', 12, 'delete_con_dpt_model'),
(48, 'Can view con_ dpt_ model', 12, 'view_con_dpt_model'),
(49, 'Can add contactos model', 13, 'add_contactosmodel'),
(50, 'Can change contactos model', 13, 'change_contactosmodel'),
(51, 'Can delete contactos model', 13, 'delete_contactosmodel'),
(52, 'Can view contactos model', 13, 'view_contactosmodel'),
(53, 'Can add departamento model', 14, 'add_departamentomodel'),
(54, 'Can change departamento model', 14, 'change_departamentomodel'),
(55, 'Can delete departamento model', 14, 'delete_departamentomodel'),
(56, 'Can view departamento model', 14, 'view_departamentomodel'),
(57, 'Can add dpt_org_ model', 15, 'add_dpt_org_model'),
(58, 'Can change dpt_org_ model', 15, 'change_dpt_org_model'),
(59, 'Can delete dpt_org_ model', 15, 'delete_dpt_org_model'),
(60, 'Can view dpt_org_ model', 15, 'view_dpt_org_model'),
(61, 'Can add <class \'User.models.User\'>', 16, 'add_historicalareasmodel'),
(62, 'Can change <class \'User.models.User\'>', 16, 'change_historicalareasmodel'),
(63, 'Can delete <class \'User.models.User\'>', 16, 'delete_historicalareasmodel'),
(64, 'Can view <class \'User.models.User\'>', 16, 'view_historicalareasmodel'),
(65, 'Can add <class \'User.models.User\'>', 17, 'add_historicalcontactosmodel'),
(66, 'Can change <class \'User.models.User\'>', 17, 'change_historicalcontactosmodel'),
(67, 'Can delete <class \'User.models.User\'>', 17, 'delete_historicalcontactosmodel'),
(68, 'Can view <class \'User.models.User\'>', 17, 'view_historicalcontactosmodel'),
(69, 'Can add <class \'User.models.User\'>', 18, 'add_historicaldepartamentomodel'),
(70, 'Can change <class \'User.models.User\'>', 18, 'change_historicaldepartamentomodel'),
(71, 'Can delete <class \'User.models.User\'>', 18, 'delete_historicaldepartamentomodel'),
(72, 'Can view <class \'User.models.User\'>', 18, 'view_historicaldepartamentomodel'),
(73, 'Can add <class \'User.models.User\'>', 19, 'add_historicalorganizacionmodel'),
(74, 'Can change <class \'User.models.User\'>', 19, 'change_historicalorganizacionmodel'),
(75, 'Can delete <class \'User.models.User\'>', 19, 'delete_historicalorganizacionmodel'),
(76, 'Can view <class \'User.models.User\'>', 19, 'view_historicalorganizacionmodel'),
(77, 'Can add organizacion model', 20, 'add_organizacionmodel'),
(78, 'Can change organizacion model', 20, 'change_organizacionmodel'),
(79, 'Can delete organizacion model', 20, 'delete_organizacionmodel'),
(80, 'Can view organizacion model', 20, 'view_organizacionmodel'),
(81, 'Can add sistema model', 21, 'add_sistemamodel'),
(82, 'Can change sistema model', 21, 'change_sistemamodel'),
(83, 'Can delete sistema model', 21, 'delete_sistemamodel'),
(84, 'Can view sistema model', 21, 'view_sistemamodel'),
(85, 'Can add tubo model', 22, 'add_tubomodel'),
(86, 'Can change tubo model', 22, 'change_tubomodel'),
(87, 'Can delete tubo model', 22, 'delete_tubomodel'),
(88, 'Can view tubo model', 22, 'view_tubomodel'),
(89, 'Can add stm_ tb_ model', 23, 'add_stm_tb_model'),
(90, 'Can change stm_ tb_ model', 23, 'change_stm_tb_model'),
(91, 'Can delete stm_ tb_ model', 23, 'delete_stm_tb_model'),
(92, 'Can view stm_ tb_ model', 23, 'view_stm_tb_model'),
(93, 'Can add <class \'User.models.User\'>', 24, 'add_historicaltubomodel'),
(94, 'Can change <class \'User.models.User\'>', 24, 'change_historicaltubomodel'),
(95, 'Can delete <class \'User.models.User\'>', 24, 'delete_historicaltubomodel'),
(96, 'Can view <class \'User.models.User\'>', 24, 'view_historicaltubomodel'),
(97, 'Can add <class \'User.models.User\'>', 25, 'add_historicalsistemamodel'),
(98, 'Can change <class \'User.models.User\'>', 25, 'change_historicalsistemamodel'),
(99, 'Can delete <class \'User.models.User\'>', 25, 'delete_historicalsistemamodel'),
(100, 'Can view <class \'User.models.User\'>', 25, 'view_historicalsistemamodel'),
(101, 'Can add cal_ med_ model', 26, 'add_cal_med_model'),
(102, 'Can change cal_ med_ model', 26, 'change_cal_med_model'),
(103, 'Can delete cal_ med_ model', 26, 'delete_cal_med_model'),
(104, 'Can view cal_ med_ model', 26, 'view_cal_med_model'),
(105, 'Can add calibraciones model', 27, 'add_calibracionesmodel'),
(106, 'Can change calibraciones model', 27, 'change_calibracionesmodel'),
(107, 'Can delete calibraciones model', 27, 'delete_calibracionesmodel'),
(108, 'Can view calibraciones model', 27, 'view_calibracionesmodel'),
(109, 'Can add <class \'User.models.User\'>', 28, 'add_historicalcalibracionesmodel'),
(110, 'Can change <class \'User.models.User\'>', 28, 'change_historicalcalibracionesmodel'),
(111, 'Can delete <class \'User.models.User\'>', 28, 'delete_historicalcalibracionesmodel'),
(112, 'Can view <class \'User.models.User\'>', 28, 'view_historicalcalibracionesmodel'),
(113, 'Can add <class \'User.models.User\'>', 29, 'add_historicalmedidoresmodel'),
(114, 'Can change <class \'User.models.User\'>', 29, 'change_historicalmedidoresmodel'),
(115, 'Can delete <class \'User.models.User\'>', 29, 'delete_historicalmedidoresmodel'),
(116, 'Can view <class \'User.models.User\'>', 29, 'view_historicalmedidoresmodel'),
(117, 'Can add medidores model', 30, 'add_medidoresmodel'),
(118, 'Can change medidores model', 30, 'change_medidoresmodel'),
(119, 'Can delete medidores model', 30, 'delete_medidoresmodel'),
(120, 'Can view medidores model', 30, 'view_medidoresmodel'),
(121, 'Can add frt_ cat_ model', 31, 'add_frt_cat_model'),
(122, 'Can change frt_ cat_ model', 31, 'change_frt_cat_model'),
(123, 'Can delete frt_ cat_ model', 31, 'delete_frt_cat_model'),
(124, 'Can view frt_ cat_ model', 31, 'view_frt_cat_model'),
(125, 'Can add reports formats model', 32, 'add_reportsformatsmodel'),
(126, 'Can change reports formats model', 32, 'change_reportsformatsmodel'),
(127, 'Can delete reports formats model', 32, 'delete_reportsformatsmodel'),
(128, 'Can view reports formats model', 32, 'view_reportsformatsmodel'),
(129, 'Can add reports reporte model', 33, 'add_reportsreportemodel'),
(130, 'Can change reports reporte model', 33, 'change_reportsreportemodel'),
(131, 'Can delete reports reporte model', 33, 'delete_reportsreportemodel'),
(132, 'Can view reports reporte model', 33, 'view_reportsreportemodel'),
(133, 'Can add rpt_ secc_ model', 34, 'add_rpt_secc_model'),
(134, 'Can change rpt_ secc_ model', 34, 'change_rpt_secc_model'),
(135, 'Can delete rpt_ secc_ model', 34, 'delete_rpt_secc_model'),
(136, 'Can view rpt_ secc_ model', 34, 'view_rpt_secc_model'),
(137, 'Can add rpt_ prt_ model', 35, 'add_rpt_prt_model'),
(138, 'Can change rpt_ prt_ model', 35, 'change_rpt_prt_model'),
(139, 'Can delete rpt_ prt_ model', 35, 'delete_rpt_prt_model'),
(140, 'Can view rpt_ prt_ model', 35, 'view_rpt_prt_model'),
(141, 'Can add rpt_ prb_ model', 36, 'add_rpt_prb_model'),
(142, 'Can change rpt_ prb_ model', 36, 'change_rpt_prb_model'),
(143, 'Can delete rpt_ prb_ model', 36, 'delete_rpt_prb_model'),
(144, 'Can view rpt_ prb_ model', 36, 'view_rpt_prb_model'),
(145, 'Can add rpt_ frt_ model', 37, 'add_rpt_frt_model'),
(146, 'Can change rpt_ frt_ model', 37, 'change_rpt_frt_model'),
(147, 'Can delete rpt_ frt_ model', 37, 'delete_rpt_frt_model'),
(148, 'Can view rpt_ frt_ model', 37, 'view_rpt_frt_model'),
(149, 'Can add reports category model', 38, 'add_reportscategorymodel'),
(150, 'Can change reports category model', 38, 'change_reportscategorymodel'),
(151, 'Can delete reports category model', 38, 'delete_reportscategorymodel'),
(152, 'Can view reports category model', 38, 'view_reportscategorymodel'),
(153, 'Can add <class \'User.models.User\'>', 39, 'add_historicalreportsreportemodel'),
(154, 'Can change <class \'User.models.User\'>', 39, 'change_historicalreportsreportemodel'),
(155, 'Can delete <class \'User.models.User\'>', 39, 'delete_historicalreportsreportemodel'),
(156, 'Can view <class \'User.models.User\'>', 39, 'view_historicalreportsreportemodel'),
(157, 'Can add <class \'User.models.User\'>', 40, 'add_historicalreportsformatsmodel'),
(158, 'Can change <class \'User.models.User\'>', 40, 'change_historicalreportsformatsmodel'),
(159, 'Can delete <class \'User.models.User\'>', 40, 'delete_historicalreportsformatsmodel'),
(160, 'Can view <class \'User.models.User\'>', 40, 'view_historicalreportsformatsmodel'),
(161, 'Can add <class \'User.models.User\'>', 41, 'add_historicalreportscategorymodel'),
(162, 'Can change <class \'User.models.User\'>', 41, 'change_historicalreportscategorymodel'),
(163, 'Can delete <class \'User.models.User\'>', 41, 'delete_historicalreportscategorymodel'),
(164, 'Can view <class \'User.models.User\'>', 41, 'view_historicalreportscategorymodel'),
(165, 'Can add cat_ category_ operaciones', 42, 'add_cat_category_operaciones'),
(166, 'Can change cat_ category_ operaciones', 42, 'change_cat_category_operaciones'),
(167, 'Can delete cat_ category_ operaciones', 42, 'delete_cat_category_operaciones'),
(168, 'Can view cat_ category_ operaciones', 42, 'view_cat_category_operaciones'),
(169, 'Can add operaciones model', 43, 'add_operacionesmodel'),
(170, 'Can change operaciones model', 43, 'change_operacionesmodel'),
(171, 'Can delete operaciones model', 43, 'delete_operacionesmodel'),
(172, 'Can view operaciones model', 43, 'view_operacionesmodel'),
(173, 'Can add variables model', 44, 'add_variablesmodel'),
(174, 'Can change variables model', 44, 'change_variablesmodel'),
(175, 'Can delete variables model', 44, 'delete_variablesmodel'),
(176, 'Can view variables model', 44, 'view_variablesmodel'),
(177, 'Can add opr_ operacion_ variables', 45, 'add_opr_operacion_variables'),
(178, 'Can change opr_ operacion_ variables', 45, 'change_opr_operacion_variables'),
(179, 'Can delete opr_ operacion_ variables', 45, 'delete_opr_operacion_variables'),
(180, 'Can view opr_ operacion_ variables', 45, 'view_opr_operacion_variables'),
(181, 'Can add <class \'User.models.User\'>', 46, 'add_historicalvariablesmodel'),
(182, 'Can change <class \'User.models.User\'>', 46, 'change_historicalvariablesmodel'),
(183, 'Can delete <class \'User.models.User\'>', 46, 'delete_historicalvariablesmodel'),
(184, 'Can view <class \'User.models.User\'>', 46, 'view_historicalvariablesmodel'),
(185, 'Can add <class \'User.models.User\'>', 47, 'add_historicaloperacionesmodel'),
(186, 'Can change <class \'User.models.User\'>', 47, 'change_historicaloperacionesmodel'),
(187, 'Can delete <class \'User.models.User\'>', 47, 'delete_historicaloperacionesmodel'),
(188, 'Can view <class \'User.models.User\'>', 47, 'view_historicaloperacionesmodel'),
(189, 'Can add <class \'User.models.User\'>', 48, 'add_historicalcategoryoperacionesmodel'),
(190, 'Can change <class \'User.models.User\'>', 48, 'change_historicalcategoryoperacionesmodel'),
(191, 'Can delete <class \'User.models.User\'>', 48, 'delete_historicalcategoryoperacionesmodel'),
(192, 'Can view <class \'User.models.User\'>', 48, 'view_historicalcategoryoperacionesmodel'),
(193, 'Can add category operaciones model', 49, 'add_categoryoperacionesmodel'),
(194, 'Can change category operaciones model', 49, 'change_categoryoperacionesmodel'),
(195, 'Can delete category operaciones model', 49, 'delete_categoryoperacionesmodel'),
(196, 'Can view category operaciones model', 49, 'view_categoryoperacionesmodel'),
(197, 'Can add prb_ calculo_ operacion_ model', 50, 'add_prb_calculo_operacion_model'),
(198, 'Can change prb_ calculo_ operacion_ model', 50, 'change_prb_calculo_operacion_model'),
(199, 'Can delete prb_ calculo_ operacion_ model', 50, 'delete_prb_calculo_operacion_model'),
(200, 'Can view prb_ calculo_ operacion_ model', 50, 'view_prb_calculo_operacion_model'),
(201, 'Can add protocols model', 51, 'add_protocolsmodel'),
(202, 'Can change protocols model', 51, 'change_protocolsmodel'),
(203, 'Can delete protocols model', 51, 'delete_protocolsmodel'),
(204, 'Can view protocols model', 51, 'view_protocolsmodel'),
(205, 'Can add prueba_ tipo_ model', 52, 'add_prueba_tipo_model'),
(206, 'Can change prueba_ tipo_ model', 52, 'change_prueba_tipo_model'),
(207, 'Can delete prueba_ tipo_ model', 52, 'delete_prueba_tipo_model'),
(208, 'Can view prueba_ tipo_ model', 52, 'view_prueba_tipo_model'),
(209, 'Can add prueba calculo model', 53, 'add_pruebacalculomodel'),
(210, 'Can change prueba calculo model', 53, 'change_pruebacalculomodel'),
(211, 'Can delete prueba calculo model', 53, 'delete_pruebacalculomodel'),
(212, 'Can view prueba calculo model', 53, 'view_pruebacalculomodel'),
(213, 'Can add prueba opciones model', 54, 'add_pruebaopcionesmodel'),
(214, 'Can change prueba opciones model', 54, 'change_pruebaopcionesmodel'),
(215, 'Can delete prueba opciones model', 54, 'delete_pruebaopcionesmodel'),
(216, 'Can view prueba opciones model', 54, 'view_pruebaopcionesmodel'),
(217, 'Can add secciones model', 55, 'add_seccionesmodel'),
(218, 'Can change secciones model', 55, 'change_seccionesmodel'),
(219, 'Can delete secciones model', 55, 'delete_seccionesmodel'),
(220, 'Can view secciones model', 55, 'view_seccionesmodel'),
(221, 'Can add prt_ scc_ model', 56, 'add_prt_scc_model'),
(222, 'Can change prt_ scc_ model', 56, 'change_prt_scc_model'),
(223, 'Can delete prt_ scc_ model', 56, 'delete_prt_scc_model'),
(224, 'Can view prt_ scc_ model', 56, 'view_prt_scc_model'),
(225, 'Can add <class \'User.models.User\'>', 57, 'add_historicalseccionesmodel'),
(226, 'Can change <class \'User.models.User\'>', 57, 'change_historicalseccionesmodel'),
(227, 'Can delete <class \'User.models.User\'>', 57, 'delete_historicalseccionesmodel'),
(228, 'Can view <class \'User.models.User\'>', 57, 'view_historicalseccionesmodel'),
(229, 'Can add <class \'User.models.User\'>', 58, 'add_historicalpruebaopcionesmodel'),
(230, 'Can change <class \'User.models.User\'>', 58, 'change_historicalpruebaopcionesmodel'),
(231, 'Can delete <class \'User.models.User\'>', 58, 'delete_historicalpruebaopcionesmodel'),
(232, 'Can view <class \'User.models.User\'>', 58, 'view_historicalpruebaopcionesmodel'),
(233, 'Can add <class \'User.models.User\'>', 59, 'add_historicalpruebacalculomodel'),
(234, 'Can change <class \'User.models.User\'>', 59, 'change_historicalpruebacalculomodel'),
(235, 'Can delete <class \'User.models.User\'>', 59, 'delete_historicalpruebacalculomodel'),
(236, 'Can view <class \'User.models.User\'>', 59, 'view_historicalpruebacalculomodel'),
(237, 'Can add <class \'User.models.User\'>', 60, 'add_historicalprotocolsmodel'),
(238, 'Can change <class \'User.models.User\'>', 60, 'change_historicalprotocolsmodel'),
(239, 'Can delete <class \'User.models.User\'>', 60, 'delete_historicalprotocolsmodel'),
(240, 'Can view <class \'User.models.User\'>', 60, 'view_historicalprotocolsmodel');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_operaciones`
--

CREATE TABLE `categoria_operaciones` (
  `CatOpr_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `categoria_id` bigint(20) NOT NULL,
  `operacion_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categoria_operaciones`
--

INSERT INTO `categoria_operaciones` (`CatOpr_id`, `created_at`, `categoria_id`, `operacion_id`) VALUES
(1, '2022-10-18 16:45:33.124296', 1, 1),
(2, '2022-10-18 16:45:33.124296', 1, 2),
(3, '2022-10-18 16:45:33.125295', 1, 3),
(4, '2022-10-18 16:45:33.125295', 1, 4),
(5, '2022-10-18 20:19:34.843812', 1, 5),
(6, '2022-10-19 00:02:35.276119', 1, 6),
(7, '2022-10-19 00:02:35.276119', 1, 7),
(8, '2022-10-19 00:02:35.276119', 1, 8),
(9, '2022-10-19 00:02:35.278117', 1, 9),
(10, '2022-10-19 00:02:35.278117', 1, 10),
(11, '2022-10-19 00:02:35.278117', 1, 11),
(12, '2022-10-19 00:02:35.278117', 1, 12),
(13, '2022-10-19 00:02:35.279116', 1, 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `companymachine_calibraciones`
--

CREATE TABLE `companymachine_calibraciones` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `cal_id` bigint(20) NOT NULL,
  `cal_fecha_calibracion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `companymachine_calibraciones`
--

INSERT INTO `companymachine_calibraciones` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `cal_id`, `cal_fecha_calibracion`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, '2020-01-28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `companymachine_calibraciones_medidores`
--

CREATE TABLE `companymachine_calibraciones_medidores` (
  `CalMed_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `calibracion_id` bigint(20) NOT NULL,
  `medidor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `companymachine_calibraciones_medidores`
--

INSERT INTO `companymachine_calibraciones_medidores` (`CalMed_id`, `created_at`, `calibracion_id`, `medidor_id`) VALUES
(2, '2022-10-19 11:40:40.065786', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `companymachine_historicalcalibracionesmodel`
--

CREATE TABLE `companymachine_historicalcalibracionesmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `cal_id` bigint(20) NOT NULL,
  `cal_fecha_calibracion` date NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `companymachine_historicalmedidoresmodel`
--

CREATE TABLE `companymachine_historicalmedidoresmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `med_id` bigint(20) NOT NULL,
  `med_marca_medidor` varchar(255) NOT NULL,
  `med_modelo_medidor` varchar(255) NOT NULL,
  `med_serie_medidor` varchar(255) NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL,
  `med_titulo_medidor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `companymachine_historicalmedidoresmodel`
--

INSERT INTO `companymachine_historicalmedidoresmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `med_id`, `med_marca_medidor`, `med_modelo_medidor`, `med_serie_medidor`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`, `med_titulo_medidor`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'RADCAL', 'RAPD-W', '01B-10-10340', 1, '2022-10-18 14:49:29.175877', NULL, '+', 1, 'Medidor Multiparámetros'),
(1, '2022-10-18', '2022-10-19', '2022-10-19', 1, 'RADCAL', 'RAPD-W', '01B-10-10340', 2, '2022-10-19 11:40:40.068784', NULL, '~', 1, 'Medidor Multiparámetros');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `companymachine_medidores`
--

CREATE TABLE `companymachine_medidores` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `med_id` bigint(20) NOT NULL,
  `med_marca_medidor` varchar(255) NOT NULL,
  `med_modelo_medidor` varchar(255) NOT NULL,
  `med_serie_medidor` varchar(255) NOT NULL,
  `med_titulo_medidor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `companymachine_medidores`
--

INSERT INTO `companymachine_medidores` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `med_id`, `med_marca_medidor`, `med_modelo_medidor`, `med_serie_medidor`, `med_titulo_medidor`) VALUES
(1, '2022-10-18', '2022-10-19', '2022-10-19', 1, 'RADCAL', 'RAPD-W', '01B-10-10340', 'Medidor Multiparámetros');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers_ambientes`
--

CREATE TABLE `customers_ambientes` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `ar_id` bigint(20) NOT NULL,
  `ar_nombre_area` varchar(255) NOT NULL,
  `ar_ubicacion_area` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`ar_ubicacion_area`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customers_ambientes`
--

INSERT INTO `customers_ambientes` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `ar_id`, `ar_nombre_area`, `ar_ubicacion_area`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'DIAGNOSTICO POR IMAGEN', '{\"piso\": \"PISO 2\", \"sala\": \"SALA  2\"}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers_contactos`
--

CREATE TABLE `customers_contactos` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `con_id` bigint(20) NOT NULL,
  `con_nombre` varchar(255) DEFAULT NULL,
  `con_apellidos` varchar(255) DEFAULT NULL,
  `con_numero_dni` varchar(255) DEFAULT NULL,
  `con_numero_telefono` varchar(255) DEFAULT NULL,
  `con_correo_electronico` varchar(255) DEFAULT NULL,
  `con_cargo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customers_contactos`
--

INSERT INTO `customers_contactos` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `con_id`, `con_nombre`, `con_apellidos`, `con_numero_dni`, `con_numero_telefono`, `con_correo_electronico`, `con_cargo`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, '---', '---', '---', '951696103', '---', '---');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers_contactos_departamento`
--

CREATE TABLE `customers_contactos_departamento` (
  `ConDpt_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `contacto_id` bigint(20) NOT NULL,
  `departamento_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customers_contactos_departamento`
--

INSERT INTO `customers_contactos_departamento` (`ConDpt_id`, `created_at`, `contacto_id`, `departamento_id`) VALUES
(1, '2022-10-19 11:17:16.507869', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers_departamento_ambiente`
--

CREATE TABLE `customers_departamento_ambiente` (
  `ArDpt_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `area_id` bigint(20) NOT NULL,
  `departamento_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers_depatamentos`
--

CREATE TABLE `customers_depatamentos` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `dpt_id` bigint(20) NOT NULL,
  `dpt_nombre_departamento` varchar(255) NOT NULL,
  `dpt_direccion_departamento` varchar(255) DEFAULT NULL,
  `dpt_pais` varchar(255) DEFAULT NULL,
  `dpt_departamento` varchar(255) DEFAULT NULL,
  `dpt_provincia` varchar(255) DEFAULT NULL,
  `dpt_distrito` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customers_depatamentos`
--

INSERT INTO `customers_depatamentos` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `dpt_id`, `dpt_nombre_departamento`, `dpt_direccion_departamento`, `dpt_pais`, `dpt_departamento`, `dpt_provincia`, `dpt_distrito`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, 'CLINICA JESUS DEL NORTE – PISO 2 – DIAGNOSTICO POR IMAGEN – SALA  2', 'AV. CARLOS IZAGUIRRE NRO.153', 'PERÚ', 'LIMA', 'LIMA', 'INDEPENDENCIA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers_organizaciones`
--

CREATE TABLE `customers_organizaciones` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `org_id` bigint(20) NOT NULL,
  `org_ruc` varchar(12) DEFAULT NULL,
  `org_razon_social` varchar(255) NOT NULL,
  `org_nombre_comercial` varchar(255) DEFAULT NULL,
  `org_tipo` varchar(255) DEFAULT NULL,
  `org_ciiu` int(11) DEFAULT NULL,
  `org_direccion_legal` varchar(255) DEFAULT NULL,
  `org_pais` varchar(255) DEFAULT NULL,
  `org_departamento` varchar(255) DEFAULT NULL,
  `org_provincia` varchar(255) DEFAULT NULL,
  `org_distrito` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customers_organizaciones`
--

INSERT INTO `customers_organizaciones` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `org_id`, `org_ruc`, `org_razon_social`, `org_nombre_comercial`, `org_tipo`, `org_ciiu`, `org_direccion_legal`, `org_pais`, `org_departamento`, `org_provincia`, `org_distrito`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, '20517738701', 'CLINICA JESUS DEL NORTE SOCIEDAD ANONIMA CERRADA', NULL, NULL, NULL, 'AV. CARLOS IZAGUIRRE NRO.153', 'PERÚ', 'LIMA', 'LIMA', 'INDEPENDENCIA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customers_organizacion_departamentos`
--

CREATE TABLE `customers_organizacion_departamentos` (
  `DptOrg_id` bigint(20) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `departamento_id` bigint(20) NOT NULL,
  `organizacion_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customers_organizacion_departamentos`
--

INSERT INTO `customers_organizacion_departamentos` (`DptOrg_id`, `created_at`, `departamento_id`, `organizacion_id`) VALUES
(1, '2022-10-19 11:17:19.278952', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customer_historicalareasmodel`
--

CREATE TABLE `customer_historicalareasmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `ar_id` bigint(20) NOT NULL,
  `ar_nombre_area` varchar(255) NOT NULL,
  `ar_ubicacion_area` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`ar_ubicacion_area`)),
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customer_historicalcontactosmodel`
--

CREATE TABLE `customer_historicalcontactosmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `con_id` bigint(20) NOT NULL,
  `con_nombre` varchar(255) DEFAULT NULL,
  `con_apellidos` varchar(255) DEFAULT NULL,
  `con_numero_dni` varchar(255) DEFAULT NULL,
  `con_numero_telefono` varchar(255) DEFAULT NULL,
  `con_correo_electronico` varchar(255) DEFAULT NULL,
  `con_cargo` varchar(255) DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customer_historicalcontactosmodel`
--

INSERT INTO `customer_historicalcontactosmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `con_id`, `con_nombre`, `con_apellidos`, `con_numero_dni`, `con_numero_telefono`, `con_correo_electronico`, `con_cargo`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, '---', '---', '---', '951696103', '---', '---', 1, '2022-10-19 11:17:11.454915', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customer_historicaldepartamentomodel`
--

CREATE TABLE `customer_historicaldepartamentomodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `dpt_id` bigint(20) NOT NULL,
  `dpt_nombre_departamento` varchar(255) NOT NULL,
  `dpt_direccion_departamento` varchar(255) DEFAULT NULL,
  `dpt_pais` varchar(255) DEFAULT NULL,
  `dpt_departamento` varchar(255) DEFAULT NULL,
  `dpt_provincia` varchar(255) DEFAULT NULL,
  `dpt_distrito` varchar(255) DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customer_historicaldepartamentomodel`
--

INSERT INTO `customer_historicaldepartamentomodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `dpt_id`, `dpt_nombre_departamento`, `dpt_direccion_departamento`, `dpt_pais`, `dpt_departamento`, `dpt_provincia`, `dpt_distrito`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, 'CLINICA JESUS DEL NORTE – PISO 2 – DIAGNOSTICO POR IMAGEN – SALA  2', 'AV. CARLOS IZAGUIRRE NRO.153', 'PERÚ', 'LIMA', 'LIMA', 'INDEPENDENCIA', 1, '2022-10-19 11:17:16.510869', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customer_historicalorganizacionmodel`
--

CREATE TABLE `customer_historicalorganizacionmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `org_id` bigint(20) NOT NULL,
  `org_ruc` varchar(12) DEFAULT NULL,
  `org_razon_social` varchar(255) NOT NULL,
  `org_nombre_comercial` varchar(255) DEFAULT NULL,
  `org_tipo` varchar(255) DEFAULT NULL,
  `org_ciiu` int(11) DEFAULT NULL,
  `org_direccion_legal` varchar(255) DEFAULT NULL,
  `org_pais` varchar(255) DEFAULT NULL,
  `org_departamento` varchar(255) DEFAULT NULL,
  `org_provincia` varchar(255) DEFAULT NULL,
  `org_distrito` varchar(255) DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customer_historicalorganizacionmodel`
--

INSERT INTO `customer_historicalorganizacionmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `org_id`, `org_ruc`, `org_razon_social`, `org_nombre_comercial`, `org_tipo`, `org_ciiu`, `org_direccion_legal`, `org_pais`, `org_departamento`, `org_provincia`, `org_distrito`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, '20517738701', 'CLINICA JESUS DEL NORTE SOCIEDAD ANONIMA CERRADA', NULL, NULL, NULL, 'AV. CARLOS IZAGUIRRE NRO.153', 'PERÚ', 'LIMA', 'LIMA', 'INDEPENDENCIA', 1, '2022-10-19 11:17:19.281954', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-10-18 15:56:16.932535', '1', '1-DB F22', 1, '[{\"added\": {}}]', 44, 1),
(2, '2022-10-18 15:56:30.321393', '2', '2-DB G22', 1, '[{\"added\": {}}]', 44, 1),
(3, '2022-10-18 15:56:43.920237', '3', '3-DB H22', 1, '[{\"added\": {}}]', 44, 1),
(4, '2022-10-18 15:56:58.383306', '4', '4-DB I22', 1, '[{\"added\": {}}]', 44, 1),
(5, '2022-10-18 15:57:52.382564', '1', '1-ALINEACIÓN DE RAYOS X/HAZ LUMINOSO .:: None ::. [4]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (1)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (2)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (3)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (4)\"}}]', 43, 1),
(6, '2022-10-18 16:02:33.922136', '5', '5-Valor de Angulación:', 1, '[{\"added\": {}}]', 44, 1),
(7, '2022-10-18 16:02:37.049522', '2', '2-ORTOGONALIDAD DEL HAZ DE RAYOS X Y DEL RECEPTOR DE IMAGEN .:: None ::. [1]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (5)\"}}]', 43, 1),
(8, '2022-10-18 16:32:28.070915', '6', '6-Diámetro Nominal (cm)', 1, '[{\"added\": {}}]', 44, 1),
(9, '2022-10-18 16:32:40.324100', '7', '7-Diámetro Medido (cm)', 1, '[{\"added\": {}}]', 44, 1),
(10, '2022-10-18 16:34:04.963116', '3', '3-Tamaño del campo de entrada del detector de imagen .:: None ::. [2]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (6)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (7)\"}}]', 43, 1),
(11, '2022-10-18 16:44:49.536957', '8', '8-Diagonal media del cuadrado mayor inscrito (mm)', 1, '[{\"added\": {}}]', 44, 1),
(12, '2022-10-18 16:44:57.909488', '9', '9-Diagonal media del cuadro central (mm)', 1, '[{\"added\": {}}]', 44, 1),
(13, '2022-10-18 16:45:19.277295', '10', '10-# de veces q el cuadrado mayor contiene al cuadrado central', 1, '[{\"added\": {}}]', 44, 1),
(14, '2022-10-18 16:45:29.980090', '4', '4-Distorsión Geométrica .:: None ::. [3]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (8)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (9)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (10)\"}}]', 43, 1),
(15, '2022-10-18 16:45:33.151279', '1', '1-Fluoroscopia', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (1)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (2)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (3)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (4)\"}}]', 49, 1),
(16, '2022-10-18 16:52:15.857423', '1', '1-Fluoroscopia', 2, '[]', 49, 1),
(17, '2022-10-18 18:01:17.546978', '1', '1-ALINEACIÓN DE RAYOS X/HAZ LUMINOSO .:: None ::. [4]', 2, '[{\"changed\": {\"fields\": [\"Operation\'s function\"]}}]', 43, 1),
(18, '2022-10-18 18:39:02.057015', '2', '2-ORTOGONALIDAD DEL HAZ DE RAYOS X Y DEL RECEPTOR DE IMAGEN .:: None ::. [1]', 2, '[{\"changed\": {\"fields\": [\"Operation\'s function\"]}}]', 43, 1),
(19, '2022-10-18 18:39:06.169548', '3', '3-Tamaño del campo de entrada del detector de imagen .:: None ::. [2]', 2, '[{\"changed\": {\"fields\": [\"Operation\'s function\"]}}]', 43, 1),
(20, '2022-10-18 18:39:10.857463', '4', '4-Distorsión Geométrica .:: None ::. [3]', 2, '[{\"changed\": {\"fields\": [\"Operation\'s function\"]}}]', 43, 1),
(21, '2022-10-18 20:14:18.678657', '11', '11-Diametro de Campo radiación en superficie de Intensificador (cm)', 1, '[{\"added\": {}}]', 44, 1),
(22, '2022-10-18 20:14:33.746709', '12', '12-Diámetro  del intensificador (cm)', 1, '[{\"added\": {}}]', 44, 1),
(23, '2022-10-18 20:14:36.276590', '5', '5-Coincidencia del  Campo de Radiación con el Área Visualizada del Detector .:: None ::. [2]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (11)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (12)\"}}]', 43, 1),
(24, '2022-10-18 20:15:17.467827', '5', '5-Coincidencia del  Campo de Radiación con el Área Visualizada del Detector .:: None ::. [2]', 2, '[{\"changed\": {\"fields\": [\"Operation\'s function\"]}}]', 43, 1),
(25, '2022-10-18 20:19:34.856259', '1', '1-Fluoroscopia', 2, '[{\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (5)\"}}]', 49, 1),
(26, '2022-10-18 20:23:09.122494', '1', '1-Alineación de rayos X / haz luminoso', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (1)\"}}]', 53, 1),
(27, '2022-10-18 20:24:10.679830', '2', '2-Ortogonalidad del haz de rayos X y del receptor de imagen', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (2)\"}}]', 53, 1),
(28, '2022-10-18 20:26:37.549061', '3', '3-Tamaño del campo de entrada del detector de imagen', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (3)\"}}]', 53, 1),
(29, '2022-10-18 20:27:39.179684', '4', '4-Distorsión Geométrica', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (4)\"}}]', 53, 1),
(30, '2022-10-18 20:29:24.457342', '5', '5-Coincidencia del campo de radiación con el área visualizada del detector', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (5)\"}}]', 53, 1),
(31, '2022-10-18 20:29:53.702669', '1', '1-PARÁMETROS GEOMÉTRICOS', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (1)\"}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (2)\"}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (3)\"}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (4)\"}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (5)\"}}]', 55, 1),
(32, '2022-10-18 20:46:30.754884', '13', '13-NOMINAL KVp', 1, '[{\"added\": {}}]', 44, 1),
(33, '2022-10-18 20:47:46.392678', '14', '14-Medidas (kVp1 - kVp2 - kVp3)', 1, '[{\"added\": {}}]', 44, 1),
(34, '2022-10-18 20:47:54.723622', '6', '6-Exactitud de la tensión .:: None ::. [2]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (13)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (14)\"}}]', 43, 1),
(35, '2022-10-18 21:02:14.147468', '7', '7-REPETIBILIDAD DE LA TENSIÓN .:: None ::. [1]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (15)\"}}]', 43, 1),
(36, '2022-10-18 21:07:08.345951', '7', '7-REPETIBILIDAD DE LA TENSIÓN .:: None ::. [1]', 2, '[{\"changed\": {\"fields\": [\"Operation\'s function\"]}}]', 43, 1),
(37, '2022-10-18 21:18:12.610229', '15', '15-Filtración total (mmAl)', 1, '[{\"added\": {}}]', 44, 1),
(38, '2022-10-18 21:18:18.677214', '8', '8-FILTRACIÓN. CAPA HEMIREDUCTORA (mmAl) .:: None ::. [1]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (16)\"}}]', 43, 1),
(39, '2022-10-18 21:31:29.581734', '16', '16-Nominal T(ms)', 1, '[{\"added\": {}}]', 44, 1),
(40, '2022-10-18 21:32:06.523342', '17', '17-Medidas (T1 - T2  - T3)', 1, '[{\"added\": {}}]', 44, 1),
(41, '2022-10-18 21:32:15.828379', '9', '9-EXACTITUD DEL TIEMPO DE EXPOSICIÓN .:: None ::. [1]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (17)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (18)\"}}]', 43, 1),
(42, '2022-10-18 21:41:05.260572', '17', '17-Medidas(ms)  (T1 - T2  - T3)', 2, '[{\"changed\": {\"fields\": [\"Variable name\"]}}]', 44, 1),
(43, '2022-10-18 21:41:06.971173', '10', '10-REPETIBILIDAD DEL TIEMPO DE EXPOSICIÓN .:: None ::. [1]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (19)\"}}]', 43, 1),
(44, '2022-10-18 23:57:45.774581', '18', '18-Medidas (uGy) (D1 - D2 - D3)', 1, '[{\"added\": {}}]', 44, 1),
(45, '2022-10-18 23:58:03.739611', '19', '19-Distancia Foco-Sensor (cm)', 1, '[{\"added\": {}}]', 44, 1),
(46, '2022-10-18 23:58:34.684633', '20', '20-Nominal (mAs) 1', 1, '[{\"added\": {}}]', 44, 1),
(47, '2022-10-18 23:58:37.068273', '11', '11-VALOR DE RENDIMIENDO .:: None ::. [3]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (20)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (21)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (22)\"}}]', 43, 1),
(48, '2022-10-18 23:59:21.457397', '12', '12-REPETIBILIDAD DEL RENDIMIENTO .:: None ::. [1]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (23)\"}}]', 43, 1),
(49, '2022-10-19 00:00:41.331735', '18', '18-Medidas (uGy) (D1 - D2 - D3) 1', 2, '[{\"changed\": {\"fields\": [\"Variable name\"]}}]', 44, 1),
(50, '2022-10-19 00:00:50.853741', '21', '21-Medidas (uGy) (D1 - D2 - D3) 2', 1, '[{\"added\": {}}]', 44, 1),
(51, '2022-10-19 00:01:38.745367', '22', '22-Nominal (mAs) 2', 1, '[{\"added\": {}}]', 44, 1),
(52, '2022-10-19 00:01:40.877690', '13', '13-VARIACIÓN DEL RENDIMIENTO LA CARGA .:: None ::. [5]', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (24)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (25)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (26)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (27)\"}}, {\"added\": {\"name\": \"opr_ operacion_ variables\", \"object\": \"Opr_Operacion_Variables object (28)\"}}]', 43, 1),
(53, '2022-10-19 00:02:35.316094', '1', '1-Fluoroscopia', 2, '[{\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (6)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (7)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (8)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (9)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (10)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (11)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (12)\"}}, {\"added\": {\"name\": \"cat_ category_ operaciones\", \"object\": \"Cat_Category_Operaciones object (13)\"}}]', 49, 1),
(54, '2022-10-19 00:04:20.237471', '1', '1-PARÁMETROS GEOMÉTRICOS', 2, '[]', 55, 1),
(55, '2022-10-19 00:05:27.510817', '6', '6-Exactitud de la tensión', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (6)\"}}]', 53, 1),
(56, '2022-10-19 00:06:11.916463', '7', '7-Repetibilidad de la tensión', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (7)\"}}]', 53, 1),
(57, '2022-10-19 00:07:31.916302', '8', '8-Filtración (Capa Hemirreductora)', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (8)\"}}]', 53, 1),
(58, '2022-10-19 00:07:36.796697', '2', '2-CALIDAD DEL HAZ', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (6)\"}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (7)\"}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (8)\"}}]', 55, 1),
(59, '2022-10-19 00:08:27.843593', '9', '9-Exactitud del tiempo de exposición', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (9)\"}}]', 53, 1),
(60, '2022-10-19 00:10:03.228198', '10', '10-Repetibilidad del tiempo de exposición', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (10)\"}}]', 53, 1),
(61, '2022-10-19 00:10:07.312238', '3', '3-TIEMPO DE EXPOSICIÓN', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (9)\"}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (10)\"}}]', 55, 1),
(62, '2022-10-19 00:11:36.728210', '11', '11-Repetibilidad del rendimiento', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prb_ calculo_ operacion_ model\", \"object\": \"Prb_Calculo_Operacion_Model object (11)\"}}]', 53, 1),
(63, '2022-10-19 00:12:09.828922', '4', '4-RENDIMIENTO', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (11)\"}}]', 55, 1),
(64, '2022-10-19 00:12:15.019319', '1', '1-Protocolo Español de Control de Calidad en Radiodiagnóstico', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (1)\"}}, {\"added\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (2)\"}}, {\"added\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (3)\"}}, {\"added\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (4)\"}}]', 51, 1),
(65, '2022-10-19 00:13:17.696475', '1', '1-CARACTERISTICA', 1, '[{\"added\": {}}]', 54, 1),
(66, '2022-10-19 00:13:20.180057', '5', '5-INDICADORES GENERALES DE FUNCIONAMIENTO Y SEGURIDAD', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"prueba_ tipo_ model\", \"object\": \"Prueba_Tipo_Model object (12)\"}}]', 55, 1),
(67, '2022-10-19 00:13:24.793438', '1', '1-Protocolo Español de Control de Calidad en Radiodiagnóstico', 2, '[{\"added\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (5)\"}}]', 51, 1),
(68, '2022-10-19 00:14:25.515632', '1', 'RADIACIÓN IONIZANTE-RI-CCRX', 1, '[{\"added\": {}}]', 38, 1),
(69, '2022-10-19 00:25:26.291200', '1', 'F1-FLUOROSCOPIA', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"rpt_ prt_ model\", \"object\": \"Rpt_Prt_Model object (1)\"}}, {\"added\": {\"name\": \"rpt_ secc_ model\", \"object\": \"Rpt_Secc_Model object (1)\"}}, {\"added\": {\"name\": \"rpt_ secc_ model\", \"object\": \"Rpt_Secc_Model object (2)\"}}, {\"added\": {\"name\": \"rpt_ secc_ model\", \"object\": \"Rpt_Secc_Model object (3)\"}}, {\"added\": {\"name\": \"rpt_ secc_ model\", \"object\": \"Rpt_Secc_Model object (4)\"}}, {\"added\": {\"name\": \"rpt_ secc_ model\", \"object\": \"Rpt_Secc_Model object (5)\"}}]', 32, 1),
(70, '2022-10-19 00:25:34.120725', '1', 'RADIACIÓN IONIZANTE-RI-CCRX', 2, '[{\"added\": {\"name\": \"frt_ cat_ model\", \"object\": \"Frt_Cat_Model object (1)\"}}]', 38, 1),
(71, '2022-10-19 00:36:42.557512', '1', '1-Protocolo Español de Control de Calidad en Radiodiagnóstico', 2, '[{\"changed\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (1)\", \"fields\": [\"Seccion\"]}}, {\"changed\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (2)\", \"fields\": [\"Seccion\"]}}, {\"changed\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (3)\", \"fields\": [\"Seccion\"]}}, {\"changed\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (4)\", \"fields\": [\"Seccion\"]}}, {\"changed\": {\"name\": \"prt_ scc_ model\", \"object\": \"Prt_Scc_Model object (5)\", \"fields\": [\"Seccion\"]}}]', 51, 1),
(72, '2022-10-19 11:17:11.460704', '1', '1--------', 1, '[{\"added\": {}}]', 13, 1),
(73, '2022-10-19 11:17:16.518878', '1', '1-CLINICA JESUS DEL NORTE – PISO 2 – DIAGNOSTICO POR IMAGEN – SALA  2', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"con_ dpt_ model\", \"object\": \"Con_Dpt_Model object (1)\"}}]', 14, 1),
(74, '2022-10-19 11:17:19.292201', '1', '1-CLINICA JESUS DEL NORTE SOCIEDAD ANONIMA CERRADA', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"dpt_org_ model\", \"object\": \"Dpt_org_Model object (1)\"}}]', 20, 1),
(75, '2022-10-19 11:18:42.429988', '1', '1TUBO-SIEMENS-OPTITOP 150/40/8O HC-100', 1, '[{\"added\": {}}]', 22, 1),
(76, '2022-10-19 11:18:44.354454', '1', '1-SIEMENS-LUMINOS FUSION FD VE 10', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"stm_ tb_ model\", \"object\": \"Stm_Tb_Model object (1)\"}}]', 21, 1),
(77, '2022-10-19 11:40:40.075874', '1', '1-RADCAL-RAPD-W', 2, '[{\"added\": {\"name\": \"cal_ med_ model\", \"object\": \"Cal_Med_Model object (2)\"}}]', 30, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(27, 'CompanyMachine', 'calibracionesmodel'),
(26, 'CompanyMachine', 'cal_med_model'),
(28, 'CompanyMachine', 'historicalcalibracionesmodel'),
(29, 'CompanyMachine', 'historicalmedidoresmodel'),
(30, 'CompanyMachine', 'medidoresmodel'),
(4, 'contenttypes', 'contenttype'),
(11, 'Customer', 'areasmodel'),
(10, 'Customer', 'ar_dpt_model'),
(13, 'Customer', 'contactosmodel'),
(12, 'Customer', 'con_dpt_model'),
(14, 'Customer', 'departamentomodel'),
(15, 'Customer', 'dpt_org_model'),
(16, 'Customer', 'historicalareasmodel'),
(17, 'Customer', 'historicalcontactosmodel'),
(18, 'Customer', 'historicaldepartamentomodel'),
(19, 'Customer', 'historicalorganizacionmodel'),
(20, 'Customer', 'organizacionmodel'),
(25, 'Machine', 'historicalsistemamodel'),
(24, 'Machine', 'historicaltubomodel'),
(21, 'Machine', 'sistemamodel'),
(23, 'Machine', 'stm_tb_model'),
(22, 'Machine', 'tubomodel'),
(49, 'Operations', 'categoryoperacionesmodel'),
(42, 'Operations', 'cat_category_operaciones'),
(48, 'Operations', 'historicalcategoryoperacionesmodel'),
(47, 'Operations', 'historicaloperacionesmodel'),
(46, 'Operations', 'historicalvariablesmodel'),
(43, 'Operations', 'operacionesmodel'),
(45, 'Operations', 'opr_operacion_variables'),
(44, 'Operations', 'variablesmodel'),
(60, 'Protocol', 'historicalprotocolsmodel'),
(59, 'Protocol', 'historicalpruebacalculomodel'),
(58, 'Protocol', 'historicalpruebaopcionesmodel'),
(57, 'Protocol', 'historicalseccionesmodel'),
(50, 'Protocol', 'prb_calculo_operacion_model'),
(51, 'Protocol', 'protocolsmodel'),
(56, 'Protocol', 'prt_scc_model'),
(53, 'Protocol', 'pruebacalculomodel'),
(54, 'Protocol', 'pruebaopcionesmodel'),
(52, 'Protocol', 'prueba_tipo_model'),
(55, 'Protocol', 'seccionesmodel'),
(31, 'Reports', 'frt_cat_model'),
(41, 'Reports', 'historicalreportscategorymodel'),
(40, 'Reports', 'historicalreportsformatsmodel'),
(39, 'Reports', 'historicalreportsreportemodel'),
(38, 'Reports', 'reportscategorymodel'),
(32, 'Reports', 'reportsformatsmodel'),
(33, 'Reports', 'reportsreportemodel'),
(37, 'Reports', 'rpt_frt_model'),
(36, 'Reports', 'rpt_prb_model'),
(35, 'Reports', 'rpt_prt_model'),
(34, 'Reports', 'rpt_secc_model'),
(5, 'sessions', 'session'),
(6, 'token_blacklist', 'blacklistedtoken'),
(7, 'token_blacklist', 'outstandingtoken'),
(9, 'User', 'historicaluser'),
(8, 'User', 'user');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-10-18 15:40:10.516659'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-10-18 15:40:10.590612'),
(3, 'auth', '0001_initial', '2022-10-18 15:40:10.861446'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-10-18 15:40:10.915413'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-10-18 15:40:10.924407'),
(6, 'auth', '0004_alter_user_username_opts', '2022-10-18 15:40:10.931403'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-10-18 15:40:10.938399'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-10-18 15:40:10.941397'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-10-18 15:40:10.951391'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-10-18 15:40:10.958386'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-10-18 15:40:10.967381'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-10-18 15:40:10.986370'),
(13, 'auth', '0011_update_proxy_permissions', '2022-10-18 15:40:11.041336'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-10-18 15:40:11.047331'),
(15, 'User', '0001_initial', '2022-10-18 15:40:11.418127'),
(16, 'CompanyMachine', '0001_initial', '2022-10-18 15:40:11.582015'),
(17, 'CompanyMachine', '0002_initial', '2022-10-18 15:40:11.819870'),
(18, 'CompanyMachine', '0003_alter_historicalcalibracionesmodel_options_and_more', '2022-10-18 15:40:11.884829'),
(19, 'CompanyMachine', '0004_alter_medidoresmodel_options', '2022-10-18 15:40:11.891826'),
(20, 'CompanyMachine', '0005_historicalmedidoresmodel_title_medidoresmodel_title', '2022-10-18 15:40:12.003765'),
(21, 'CompanyMachine', '0006_alter_historicalmedidoresmodel_title_and_more', '2022-10-18 15:40:12.019748'),
(22, 'Customer', '0001_initial', '2022-10-18 15:40:12.407018'),
(23, 'Customer', '0002_initial', '2022-10-18 15:40:12.980604'),
(24, 'Customer', '0003_alter_historicalareasmodel_options_and_more', '2022-10-18 15:40:13.142505'),
(25, 'Customer', '0004_alter_contactosmodel_apellidos_and_more', '2022-10-18 15:40:13.677365'),
(26, 'Customer', '0005_alter_contactosmodel_dni_and_more', '2022-10-18 15:40:13.872418'),
(27, 'Machine', '0001_initial', '2022-10-18 15:40:14.289470'),
(28, 'Machine', '0002_alter_historicaltubomodel_title_and_more', '2022-10-18 15:40:14.315454'),
(29, 'Operations', '0001_initial', '2022-10-18 15:40:15.193826'),
(30, 'Protocol', '0001_initial', '2022-10-18 15:40:16.425068'),
(31, 'Reports', '0001_initial', '2022-10-18 15:40:17.862833'),
(32, 'User', '0002_alter_historicaluser_options_and_more', '2022-10-18 15:40:18.013741'),
(33, 'admin', '0001_initial', '2022-10-18 15:40:18.152657'),
(34, 'admin', '0002_logentry_remove_auto_add', '2022-10-18 15:40:18.185637'),
(35, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-18 15:40:18.218617'),
(36, 'sessions', '0001_initial', '2022-10-18 15:40:18.258592'),
(37, 'token_blacklist', '0001_initial', '2022-10-18 15:40:18.438717'),
(38, 'token_blacklist', '0002_outstandingtoken_jti_hex', '2022-10-18 15:40:18.484315'),
(39, 'token_blacklist', '0003_auto_20171017_2007', '2022-10-18 15:40:18.544278'),
(40, 'token_blacklist', '0004_auto_20171017_2013', '2022-10-18 15:40:18.663850'),
(41, 'token_blacklist', '0005_remove_outstandingtoken_jti', '2022-10-18 15:40:18.710187'),
(42, 'token_blacklist', '0006_auto_20171017_2113', '2022-10-18 15:40:18.763155'),
(43, 'token_blacklist', '0007_auto_20171017_2214', '2022-10-18 15:40:19.098264'),
(44, 'token_blacklist', '0008_migrate_to_bigautofield', '2022-10-18 15:40:19.410619'),
(45, 'token_blacklist', '0010_fix_migrate_to_bigautofield', '2022-10-18 15:40:19.449595'),
(46, 'token_blacklist', '0011_linearizes_history', '2022-10-18 15:40:19.452960'),
(47, 'token_blacklist', '0012_alter_outstandingtoken_user', '2022-10-18 15:40:19.486940'),
(48, 'Operations', '0002_alter_historicalvariablesmodel_nombre_variable_and_more', '2022-10-18 15:53:23.582486'),
(49, 'Reports', '0002_remove_reportsformatsmodel_calculo_and_more', '2022-10-19 00:29:31.144633');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('su7yy29x4vw0snt2owv3643855t2uz4n', '.eJxVjMsOwiAQRf-FtSFleLt0328gMINSNZCUdmX8dyXpQrf3nHNfLMR9K2HveQ0LsTMT7PS7pYiPXAege6y3xrHVbV0SHwo_aOdzo_y8HO7fQYm9fGuvUCd1tThpo0g4AAPagASvXBYOMXtLymtNMDk1TLAgMQoQUjhN7P0BsQQ2Ww:1okoj9:h66LpYLwzS2Cye6NofS1-UhkWlLCAeNsu_Y2EIfzprI', '2022-11-01 15:41:59.910295');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `machines_sistemas`
--

CREATE TABLE `machines_sistemas` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `stm_id` bigint(20) NOT NULL,
  `stm_marca_sistema` varchar(255) NOT NULL,
  `stm_modelo_sistema` varchar(255) NOT NULL,
  `stm_serie_sistema` varchar(255) NOT NULL,
  `stm_antiguedad_sistema` date DEFAULT NULL,
  `stm_year_sistema` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `machines_sistemas`
--

INSERT INTO `machines_sistemas` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `stm_id`, `stm_marca_sistema`, `stm_modelo_sistema`, `stm_serie_sistema`, `stm_antiguedad_sistema`, `stm_year_sistema`) VALUES
(0, '2022-10-19', '2022-10-19', '2022-10-19', 1, 'SIEMENS', 'LUMINOS FUSION FD VE 10', '31161', '2018-01-01', '2018-01-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `machines_tubos`
--

CREATE TABLE `machines_tubos` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `tb_id` bigint(20) NOT NULL,
  `tb_title_componente` varchar(255) NOT NULL,
  `tb_marca_componente` varchar(255) NOT NULL,
  `tb_modelo_componente` varchar(255) NOT NULL,
  `tb_serie_componente` varchar(255) NOT NULL,
  `tb_antiguedad_tcomponente` date DEFAULT NULL,
  `tb_year_componente` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `machines_tubos`
--

INSERT INTO `machines_tubos` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `tb_id`, `tb_title_componente`, `tb_marca_componente`, `tb_modelo_componente`, `tb_serie_componente`, `tb_antiguedad_tcomponente`, `tb_year_componente`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, 'TUBO', 'SIEMENS', 'OPTITOP 150/40/8O HC-100', '421501771', '2018-01-01', '2018-01-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `machine_historicalsistemamodel`
--

CREATE TABLE `machine_historicalsistemamodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `stm_id` bigint(20) NOT NULL,
  `stm_marca_sistema` varchar(255) NOT NULL,
  `stm_modelo_sistema` varchar(255) NOT NULL,
  `stm_serie_sistema` varchar(255) NOT NULL,
  `stm_antiguedad_sistema` date DEFAULT NULL,
  `stm_year_sistema` date DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `machine_historicalsistemamodel`
--

INSERT INTO `machine_historicalsistemamodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `stm_id`, `stm_marca_sistema`, `stm_modelo_sistema`, `stm_serie_sistema`, `stm_antiguedad_sistema`, `stm_year_sistema`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(0, '2022-10-19', '2022-10-19', '2022-10-19', 1, 'SIEMENS', 'LUMINOS FUSION FD VE 10', '31161', '2018-01-01', '2018-01-01', 1, '2022-10-19 11:18:44.344967', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `machine_historicaltubomodel`
--

CREATE TABLE `machine_historicaltubomodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `tb_id` bigint(20) NOT NULL,
  `tb_title_componente` varchar(255) NOT NULL,
  `tb_marca_componente` varchar(255) NOT NULL,
  `tb_modelo_componente` varchar(255) NOT NULL,
  `tb_serie_componente` varchar(255) NOT NULL,
  `tb_antiguedad_tcomponente` date DEFAULT NULL,
  `tb_year_componente` date DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `machine_historicaltubomodel`
--

INSERT INTO `machine_historicaltubomodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `tb_id`, `tb_title_componente`, `tb_marca_componente`, `tb_modelo_componente`, `tb_serie_componente`, `tb_antiguedad_tcomponente`, `tb_year_componente`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-19', '2022-10-19', '2022-10-19', 1, 'TUBO', 'SIEMENS', 'OPTITOP 150/40/8O HC-100', '421501771', '2018-01-01', '2018-01-01', 1, '2022-10-19 11:18:42.424351', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operacion_variables`
--

CREATE TABLE `operacion_variables` (
  `OprVar_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `operacion_id` bigint(20) NOT NULL,
  `variables_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operacion_variables`
--

INSERT INTO `operacion_variables` (`OprVar_id`, `created_at`, `operacion_id`, `variables_id`) VALUES
(1, '2022-10-18 15:57:52.362244', 1, 1),
(2, '2022-10-18 15:57:52.363263', 1, 2),
(3, '2022-10-18 15:57:52.363263', 1, 3),
(4, '2022-10-18 15:57:52.363263', 1, 4),
(5, '2022-10-18 16:02:37.039699', 2, 5),
(6, '2022-10-18 16:34:04.955119', 3, 6),
(7, '2022-10-18 16:34:04.956123', 3, 7),
(8, '2022-10-18 16:45:29.960811', 4, 8),
(9, '2022-10-18 16:45:29.961810', 4, 9),
(10, '2022-10-18 16:45:29.961810', 4, 10),
(11, '2022-10-18 20:14:36.263451', 5, 11),
(12, '2022-10-18 20:14:36.264448', 5, 12),
(13, '2022-10-18 20:47:54.709474', 6, 13),
(14, '2022-10-18 20:47:54.709474', 6, 14),
(15, '2022-10-18 21:02:14.139399', 7, 14),
(16, '2022-10-18 21:18:18.667083', 8, 15),
(17, '2022-10-18 21:32:15.821665', 9, 16),
(18, '2022-10-18 21:32:15.822664', 9, 17),
(19, '2022-10-18 21:41:06.966816', 10, 17),
(20, '2022-10-18 23:58:37.053283', 11, 18),
(21, '2022-10-18 23:58:37.054282', 11, 19),
(22, '2022-10-18 23:58:37.054282', 11, 20),
(23, '2022-10-18 23:59:21.452388', 12, 18),
(24, '2022-10-19 00:01:40.861697', 13, 18),
(25, '2022-10-19 00:01:40.862698', 13, 21),
(26, '2022-10-19 00:01:40.862698', 13, 19),
(27, '2022-10-19 00:01:40.862698', 13, 20),
(28, '2022-10-19 00:01:40.862698', 13, 22);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operations_categorias_operaciones`
--

CREATE TABLE `operations_categorias_operaciones` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `cat_opr_id` bigint(20) NOT NULL,
  `cat_opr_titulo` varchar(255) NOT NULL,
  `cat_opr_contexto` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operations_categorias_operaciones`
--

INSERT INTO `operations_categorias_operaciones` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `cat_opr_id`, `cat_opr_titulo`, `cat_opr_contexto`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Fluoroscopia', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operations_historicalcategoryoperacionesmodel`
--

CREATE TABLE `operations_historicalcategoryoperacionesmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `cat_opr_id` bigint(20) NOT NULL,
  `cat_opr_titulo` varchar(255) NOT NULL,
  `cat_opr_contexto` longtext DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operations_historicalcategoryoperacionesmodel`
--

INSERT INTO `operations_historicalcategoryoperacionesmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `cat_opr_id`, `cat_opr_titulo`, `cat_opr_contexto`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Fluoroscopia', '', 1, '2022-10-18 16:45:33.139287', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Fluoroscopia', '', 2, '2022-10-18 16:52:15.853427', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Fluoroscopia', '', 3, '2022-10-18 20:19:34.854118', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Fluoroscopia', '', 4, '2022-10-19 00:02:35.303101', NULL, '~', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operations_historicaloperacionesmodel`
--

CREATE TABLE `operations_historicaloperacionesmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `opr_id` bigint(20) NOT NULL,
  `opr_titulo` varchar(255) NOT NULL,
  `opr_funcion` varchar(255) NOT NULL,
  `opr_simbolo` varchar(255) DEFAULT NULL,
  `opr_cantidad_variables` int(11) NOT NULL,
  `opr_contexto` longtext NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operations_historicaloperacionesmodel`
--

INSERT INTO `operations_historicaloperacionesmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `opr_id`, `opr_titulo`, `opr_funcion`, `opr_simbolo`, `opr_cantidad_variables`, `opr_contexto`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'ALINEACIÓN DE RAYOS X/HAZ LUMINOSO', 'alineacion_rayos_x_haz_luminoso', NULL, 4, '', 1, '2022-10-18 15:57:52.371059', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'ORTOGONALIDAD DEL HAZ DE RAYOS X Y DEL RECEPTOR DE IMAGEN', 'ortogonalidad_haz_rayos_x_receptor_imagen', NULL, 1, '', 2, '2022-10-18 16:02:37.042937', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'Tamaño del campo de entrada del detector de imagen', 'tamano_campo_entrada_detector_imagen', NULL, 2, '', 3, '2022-10-18 16:34:04.961116', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'Distorsión Geométrica', 'distorsion_geometrica', NULL, 3, '', 4, '2022-10-18 16:45:29.969898', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'ALINEACIÓN DE RAYOS X/HAZ LUMINOSO', 'fluoroscopia_alineacion_rayos_x_haz_luminoso', NULL, 4, '', 5, '2022-10-18 18:01:17.542585', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'ORTOGONALIDAD DEL HAZ DE RAYOS X Y DEL RECEPTOR DE IMAGEN', 'fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen', NULL, 1, '', 6, '2022-10-18 18:39:02.051019', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'Tamaño del campo de entrada del detector de imagen', 'fluoroscopia_tamano_campo_entrada_detector_imagen', NULL, 2, '', 7, '2022-10-18 18:39:06.168546', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'Distorsión Geométrica', 'fluoroscopia_distorsion_geometrica', NULL, 3, '', 8, '2022-10-18 18:39:10.855465', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'Coincidencia del  Campo de Radiación con el Área Visualizada del Detector', 'coincidencia_campo_radiacion_area_visualizada_detector', NULL, 2, '', 9, '2022-10-18 20:14:36.270548', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'Coincidencia del  Campo de Radiación con el Área Visualizada del Detector', 'fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector', NULL, 2, '', 10, '2022-10-18 20:15:17.464621', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 6, 'Exactitud de la tensión', 'fluoroscopia_exactitud_tension', NULL, 2, '', 11, '2022-10-18 20:47:54.714471', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 7, 'REPETIBILIDAD DE LA TENSIÓN', 'fluoroscopia_repetibilidad_tension.py', NULL, 1, '', 12, '2022-10-18 21:02:14.143349', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 7, 'REPETIBILIDAD DE LA TENSIÓN', 'fluoroscopia_repetibilidad_tension', NULL, 1, '', 13, '2022-10-18 21:07:08.343953', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 8, 'FILTRACIÓN. CAPA HEMIREDUCTORA (mmAl)', 'fluoroscopia_filtracion_capa_hemireductora', NULL, 1, '', 14, '2022-10-18 21:18:18.671082', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 9, 'EXACTITUD DEL TIEMPO DE EXPOSICIÓN', 'fluoroscopia_exactitud_tiempo_exposicion', NULL, 1, '', 15, '2022-10-18 21:32:15.826289', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 10, 'REPETIBILIDAD DEL TIEMPO DE EXPOSICIÓN', 'fluoroscopia_repetibilidad_tiempo_exposicion', NULL, 1, '', 16, '2022-10-18 21:41:06.969714', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 11, 'VALOR DE RENDIMIENDO', 'fluoroscopia_valor_rendimiento', NULL, 3, '', 17, '2022-10-18 23:58:37.060278', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 12, 'REPETIBILIDAD DEL RENDIMIENTO', 'fluoroscopia_repetibilidad_rendimiento', NULL, 1, '', 18, '2022-10-18 23:59:21.456417', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 13, 'VARIACIÓN DEL RENDIMIENTO LA CARGA', 'fluoroscopia_variacion_rendimiento_carga', NULL, 5, '', 19, '2022-10-19 00:01:40.870691', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operations_historicalvariablesmodel`
--

CREATE TABLE `operations_historicalvariablesmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `var_id` bigint(20) NOT NULL,
  `var_nombre` varchar(255) NOT NULL,
  `var_range` int(11) NOT NULL,
  `var_valor_defecto` int(11) DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operations_historicalvariablesmodel`
--

INSERT INTO `operations_historicalvariablesmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `var_id`, `var_nombre`, `var_range`, `var_valor_defecto`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'DB F22', 1, NULL, 1, '2022-10-18 15:56:16.929701', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'DB G22', 1, NULL, 2, '2022-10-18 15:56:30.318395', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'DB H22', 1, NULL, 3, '2022-10-18 15:56:43.919238', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'DB I22', 1, NULL, 4, '2022-10-18 15:56:58.380306', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'Valor de Angulación:', 1, NULL, 5, '2022-10-18 16:02:33.921138', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 6, 'Diámetro Nominal (cm)', 3, NULL, 6, '2022-10-18 16:32:28.067918', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 7, 'Diámetro Medido (cm)', 3, NULL, 7, '2022-10-18 16:32:40.323098', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 8, 'Diagonal media del cuadrado mayor inscrito (mm)', 1, NULL, 8, '2022-10-18 16:44:49.533960', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 9, 'Diagonal media del cuadro central (mm)', 1, NULL, 9, '2022-10-18 16:44:57.908544', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 10, '# de veces q el cuadrado mayor contiene al cuadrado central', 1, NULL, 10, '2022-10-18 16:45:19.275296', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 11, 'Diametro de Campo radiación en superficie de Intensificador (cm)', 1, NULL, 11, '2022-10-18 20:14:18.673561', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 12, 'Diámetro  del intensificador (cm)', 1, NULL, 12, '2022-10-18 20:14:33.745541', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 13, 'NOMINAL KVp', 1, NULL, 13, '2022-10-18 20:46:30.753880', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 14, 'Medidas (kVp1 - kVp2 - kVp3)', 3, NULL, 14, '2022-10-18 20:47:46.389677', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 15, 'Filtración total (mmAl)', 3, NULL, 15, '2022-10-18 21:18:12.608231', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 16, 'Nominal T(ms)', 1, NULL, 16, '2022-10-18 21:31:29.579737', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 17, 'Medidas (T1 - T2  - T3)', 3, NULL, 17, '2022-10-18 21:32:06.520170', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 17, 'Medidas(ms)  (T1 - T2  - T3)', 3, NULL, 18, '2022-10-18 21:41:05.258574', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 18, 'Medidas (uGy) (D1 - D2 - D3)', 3, NULL, 19, '2022-10-18 23:57:45.773582', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 19, 'Distancia Foco-Sensor (cm)', 1, NULL, 20, '2022-10-18 23:58:03.735612', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 20, 'Nominal (mAs) 1', 1, NULL, 21, '2022-10-18 23:58:34.682911', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 18, 'Medidas (uGy) (D1 - D2 - D3) 1', 3, NULL, 22, '2022-10-19 00:00:41.330739', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 21, 'Medidas (uGy) (D1 - D2 - D3) 2', 3, NULL, 23, '2022-10-19 00:00:50.851741', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 22, 'Nominal (mAs) 2', 1, NULL, 24, '2022-10-19 00:01:38.742368', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operations_operaciones`
--

CREATE TABLE `operations_operaciones` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `opr_id` bigint(20) NOT NULL,
  `opr_titulo` varchar(255) NOT NULL,
  `opr_funcion` varchar(255) NOT NULL,
  `opr_simbolo` varchar(255) DEFAULT NULL,
  `opr_cantidad_variables` int(11) NOT NULL,
  `opr_contexto` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operations_operaciones`
--

INSERT INTO `operations_operaciones` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `opr_id`, `opr_titulo`, `opr_funcion`, `opr_simbolo`, `opr_cantidad_variables`, `opr_contexto`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'ALINEACIÓN DE RAYOS X/HAZ LUMINOSO', 'fluoroscopia_alineacion_rayos_x_haz_luminoso', NULL, 4, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'ORTOGONALIDAD DEL HAZ DE RAYOS X Y DEL RECEPTOR DE IMAGEN', 'fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen', NULL, 1, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'Tamaño del campo de entrada del detector de imagen', 'fluoroscopia_tamano_campo_entrada_detector_imagen', NULL, 2, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'Distorsión Geométrica', 'fluoroscopia_distorsion_geometrica', NULL, 3, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'Coincidencia del  Campo de Radiación con el Área Visualizada del Detector', 'fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector', NULL, 2, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 6, 'Exactitud de la tensión', 'fluoroscopia_exactitud_tension', NULL, 2, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 7, 'REPETIBILIDAD DE LA TENSIÓN', 'fluoroscopia_repetibilidad_tension', NULL, 1, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 8, 'FILTRACIÓN. CAPA HEMIREDUCTORA (mmAl)', 'fluoroscopia_filtracion_capa_hemireductora', NULL, 1, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 9, 'EXACTITUD DEL TIEMPO DE EXPOSICIÓN', 'fluoroscopia_exactitud_tiempo_exposicion', NULL, 1, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 10, 'REPETIBILIDAD DEL TIEMPO DE EXPOSICIÓN', 'fluoroscopia_repetibilidad_tiempo_exposicion', NULL, 1, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 11, 'VALOR DE RENDIMIENDO', 'fluoroscopia_valor_rendimiento', NULL, 3, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 12, 'REPETIBILIDAD DEL RENDIMIENTO', 'fluoroscopia_repetibilidad_rendimiento', NULL, 1, ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 13, 'VARIACIÓN DEL RENDIMIENTO LA CARGA', 'fluoroscopia_variacion_rendimiento_carga', NULL, 5, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operations_variables`
--

CREATE TABLE `operations_variables` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `var_id` bigint(20) NOT NULL,
  `var_nombre` varchar(255) NOT NULL,
  `var_range` int(11) NOT NULL,
  `var_valor_defecto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `operations_variables`
--

INSERT INTO `operations_variables` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `var_id`, `var_nombre`, `var_range`, `var_valor_defecto`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'DB F22', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'DB G22', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'DB H22', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'DB I22', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'Valor de Angulación:', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 6, 'Diámetro Nominal (cm)', 3, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 7, 'Diámetro Medido (cm)', 3, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 8, 'Diagonal media del cuadrado mayor inscrito (mm)', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 9, 'Diagonal media del cuadro central (mm)', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 10, '# de veces q el cuadrado mayor contiene al cuadrado central', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 11, 'Diametro de Campo radiación en superficie de Intensificador (cm)', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 12, 'Diámetro  del intensificador (cm)', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 13, 'NOMINAL KVp', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 14, 'Medidas (kVp1 - kVp2 - kVp3)', 3, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 15, 'Filtración total (mmAl)', 3, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 16, 'Nominal T(ms)', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 17, 'Medidas(ms)  (T1 - T2  - T3)', 3, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 18, 'Medidas (uGy) (D1 - D2 - D3) 1', 3, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 19, 'Distancia Foco-Sensor (cm)', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 20, 'Nominal (mAs) 1', 1, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 21, 'Medidas (uGy) (D1 - D2 - D3) 2', 3, NULL),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 22, 'Nominal (mAs) 2', 1, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `protocols_protocolos`
--

CREATE TABLE `protocols_protocolos` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `prt_id` bigint(20) NOT NULL,
  `prt_nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `protocols_protocolos`
--

INSERT INTO `protocols_protocolos` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `prt_id`, `prt_nombre`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Protocolo Español de Control de Calidad en Radiodiagnóstico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `protocols_protocolo_secciones`
--

CREATE TABLE `protocols_protocolo_secciones` (
  `PrtScc_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `protocolo_id` bigint(20) NOT NULL,
  `seccion_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `protocols_protocolo_secciones`
--

INSERT INTO `protocols_protocolo_secciones` (`PrtScc_id`, `created_at`, `protocolo_id`, `seccion_id`) VALUES
(1, '2022-10-19 00:12:15.000331', 1, 5),
(2, '2022-10-19 00:12:15.000331', 1, 1),
(3, '2022-10-19 00:12:15.001331', 1, 2),
(4, '2022-10-19 00:12:15.001331', 1, 3),
(5, '2022-10-19 00:13:24.777561', 1, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `protocols_secciones`
--

CREATE TABLE `protocols_secciones` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `scc_id` bigint(20) NOT NULL,
  `scc_nombre` varchar(255) NOT NULL,
  `scc_contexto` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `protocols_secciones`
--

INSERT INTO `protocols_secciones` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `scc_id`, `scc_nombre`, `scc_contexto`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'PARÁMETROS GEOMÉTRICOS', ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'CALIDAD DEL HAZ', ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'TIEMPO DE EXPOSICIÓN', ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'RENDIMIENTO', ''),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'INDICADORES GENERALES DE FUNCIONAMIENTO Y SEGURIDAD', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `protocol_historicalprotocolsmodel`
--

CREATE TABLE `protocol_historicalprotocolsmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `prt_id` bigint(20) NOT NULL,
  `prt_nombre` varchar(255) NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `protocol_historicalprotocolsmodel`
--

INSERT INTO `protocol_historicalprotocolsmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `prt_id`, `prt_nombre`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Protocolo Español de Control de Calidad en Radiodiagnóstico', 1, '2022-10-19 00:12:15.009326', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Protocolo Español de Control de Calidad en Radiodiagnóstico', 2, '2022-10-19 00:13:24.787559', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Protocolo Español de Control de Calidad en Radiodiagnóstico', 3, '2022-10-19 00:36:42.545760', NULL, '~', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `protocol_historicalpruebacalculomodel`
--

CREATE TABLE `protocol_historicalpruebacalculomodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `prb_cal_id` bigint(20) NOT NULL,
  `prb_cal_titulo` varchar(255) NOT NULL,
  `prb_cal_contexto` longtext DEFAULT NULL,
  `prb_cal_resultado` longtext DEFAULT NULL,
  `prb_cal_tolerancia` longtext NOT NULL,
  `prb_cal_condicion_respuesta` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`prb_cal_condicion_respuesta`)),
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `protocol_historicalpruebacalculomodel`
--

INSERT INTO `protocol_historicalpruebacalculomodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `prb_cal_id`, `prb_cal_titulo`, `prb_cal_contexto`, `prb_cal_resultado`, `prb_cal_tolerancia`, `prb_cal_condicion_respuesta`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Alineación de rayos X / haz luminoso', '', '', 'Suma de las desviaciones en los bordes inferiores 2.0% de la distancia entre el foco y el maniquí de colimación para cada dirección principal. La suma total de las desviaciones no excederá el 3% de la distancia entre el foco y el maniquí de colimación.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 1, '2022-10-18 20:23:09.117424', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'Ortogonalidad del haz de rayos X y del receptor de imagen', '', '', 'El ángulo que forman el eje central del haz de rayos X y el plano del receptor de imagen no deberá desviarse de los 90° más de 1.5°.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 2, '2022-10-18 20:24:10.673219', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'Tamaño del campo de entrada del detector de imagen', '', '', 'Para campos circulares: DM/DN ≥ 0.85. Para campos rectangulares sustituir el diámetro por la diagonal media.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 3, '2022-10-18 20:26:37.548059', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'Distorsión Geométrica', '', '', '≤ 10%', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 4, '2022-10-18 20:27:39.174533', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'Coincidencia del campo de radiación con el área visualizada del detector', '', '', 'La relación entre el área del campo de radiación y el área visualizada en la superficie de entrada del detector de imagen debe ser ≤ 1.15', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 5, '2022-10-18 20:29:24.455205', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 6, 'Exactitud de la tensión', '', '', 'Desviación con respecto al valor nominal < ±10%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 6, '2022-10-19 00:05:27.502017', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 7, 'Repetibilidad de la tensión', '', '', 'Coeficiente de variación < 5%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 7, '2022-10-19 00:06:11.914463', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 8, 'Filtración (Capa Hemirreductora)', '', '', '> 2.5 mmAl (a 70 kVp) y >2.9 mmAl (a 80 kVp)', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 8, '2022-10-19 00:07:31.910306', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 9, 'Exactitud del tiempo de exposición', '', '', 'Desviación con respecto al valor nominal < ±10% para tiempos > 20 ms y lo especificado por el fabricante para tiempos ≤ 20 ms', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 9, '2022-10-19 00:08:27.841649', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 10, 'Repetibilidad del tiempo de exposición', '', '', 'Coeficiente de variación < 10%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 10, '2022-10-19 00:10:03.226364', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 11, 'Repetibilidad del rendimiento', '', '', 'Coeficiente de variación < 10%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}', 11, '2022-10-19 00:11:36.722212', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `protocol_historicalpruebaopcionesmodel`
--

CREATE TABLE `protocol_historicalpruebaopcionesmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `prb_opc_id` bigint(20) NOT NULL,
  `prb_opc_titulo` varchar(255) NOT NULL,
  `prb_opc_contexto` longtext DEFAULT NULL,
  `prb_opc_resultado` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`prb_opc_resultado`)),
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `protocol_historicalpruebaopcionesmodel`
--

INSERT INTO `protocol_historicalpruebaopcionesmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `prb_opc_id`, `prb_opc_titulo`, `prb_opc_contexto`, `prb_opc_resultado`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'CARACTERISTICA', '', '[{\"opcion\": \"ESTABILIDAD MECANICA\"}, {\"opcion\": \"MOVIMIENTOS ADECUADOS DEL EQUIPO\"}, {\"opcion\": \"BUEN ESTADO DE LOS CABLES (ALTA TENSION Y ALIMENTACION)\"}, {\"opcion\": \"EXISTE INDICADOR DEL PUNTO FOCAL\"}, {\"opcion\": \"LOS INDICADORES DE TECNICA DE EXPOSICION EN EL PANEL DE CONTROL FUNCIONAN ADECUADAMENTE\"}, {\"opcion\": \"EXISTE SE\\u00d1AL AUDIBLE DURANTE Y/O AL FINAL DE LA EXPOSICION \"}, {\"opcion\": \"EXISTE INTERRUPTOR DE EXPOSICION TIPO HOMBRE MUERTO\"}, {\"opcion\": \"EXISTE INTERRUPTOR DE EXPOSICION TIPO PEDAL DE DISPARO\"}]', 1, '2022-10-19 00:13:17.692474', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `protocol_historicalseccionesmodel`
--

CREATE TABLE `protocol_historicalseccionesmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `scc_id` bigint(20) NOT NULL,
  `scc_nombre` varchar(255) NOT NULL,
  `scc_contexto` longtext DEFAULT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `protocol_historicalseccionesmodel`
--

INSERT INTO `protocol_historicalseccionesmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `scc_id`, `scc_nombre`, `scc_contexto`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'PARÁMETROS GEOMÉTRICOS', '', 1, '2022-10-18 20:29:53.692523', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'PARÁMETROS GEOMÉTRICOS', '', 2, '2022-10-19 00:04:20.233475', NULL, '~', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'CALIDAD DEL HAZ', '', 3, '2022-10-19 00:07:36.788697', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'TIEMPO DE EXPOSICIÓN', '', 4, '2022-10-19 00:10:07.305004', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'RENDIMIENTO', '', 5, '2022-10-19 00:12:09.824924', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'INDICADORES GENERALES DE FUNCIONAMIENTO Y SEGURIDAD', '', 6, '2022-10-19 00:13:20.175377', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_categorias`
--

CREATE TABLE `reports_categorias` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `rep_cat_id` bigint(20) NOT NULL,
  `rep_cat_area` varchar(255) NOT NULL,
  `rep_cat_abreviatura` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_categorias`
--

INSERT INTO `reports_categorias` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `rep_cat_id`, `rep_cat_area`, `rep_cat_abreviatura`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'RADIACIÓN IONIZANTE', 'RI-CCRX');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_formatos`
--

CREATE TABLE `reports_formatos` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `rep_frt_id` bigint(20) NOT NULL,
  `rep_frt_codigo` varchar(255) DEFAULT NULL,
  `rep_frt_nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_formatos`
--

INSERT INTO `reports_formatos` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `rep_frt_id`, `rep_frt_codigo`, `rep_frt_nombre`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'F1', 'FLUOROSCOPIA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_formatos_categoria`
--

CREATE TABLE `reports_formatos_categoria` (
  `FrtCat_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `categoria_id` bigint(20) NOT NULL,
  `formatos_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_formatos_categoria`
--

INSERT INTO `reports_formatos_categoria` (`FrtCat_id`, `created_at`, `categoria_id`, `formatos_id`) VALUES
(1, '2022-10-19 00:25:34.111551', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_historicalreportscategorymodel`
--

CREATE TABLE `reports_historicalreportscategorymodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `rep_cat_id` bigint(20) NOT NULL,
  `rep_cat_area` varchar(255) NOT NULL,
  `rep_cat_abreviatura` varchar(255) NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_historicalreportscategorymodel`
--

INSERT INTO `reports_historicalreportscategorymodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `rep_cat_id`, `rep_cat_area`, `rep_cat_abreviatura`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'RADIACIÓN IONIZANTE', 'RI-CCRX', 1, '2022-10-19 00:14:25.510636', NULL, '+', 1),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'RADIACIÓN IONIZANTE', 'RI-CCRX', 2, '2022-10-19 00:25:34.115723', NULL, '~', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_historicalreportsformatsmodel`
--

CREATE TABLE `reports_historicalreportsformatsmodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `rep_frt_id` bigint(20) NOT NULL,
  `rep_frt_codigo` varchar(255) DEFAULT NULL,
  `rep_frt_nombre` varchar(255) NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_historicalreportsformatsmodel`
--

INSERT INTO `reports_historicalreportsformatsmodel` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `rep_frt_id`, `rep_frt_codigo`, `rep_frt_nombre`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'F1', 'FLUOROSCOPIA', 1, '2022-10-19 00:25:26.275231', NULL, '+', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_historicalreportsreportemodel`
--

CREATE TABLE `reports_historicalreportsreportemodel` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `rpt_id` bigint(20) NOT NULL,
  `rpt_numero_orden_trabajo` varchar(255) NOT NULL,
  `rpt_fecha_control_calidad` date NOT NULL,
  `rpt_data_clientes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_clientes`)),
  `rpt_data_sistema` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_sistema`)),
  `rpt_data_component` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_component`)),
  `rpt_data_maquina` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_maquina`)),
  `rpt_valores_operaciones` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_valores_operaciones`)),
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_reportes`
--

CREATE TABLE `reports_reportes` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `rpt_id` bigint(20) NOT NULL,
  `rpt_numero_orden_trabajo` varchar(255) NOT NULL,
  `rpt_fecha_control_calidad` date NOT NULL,
  `rpt_data_clientes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_clientes`)),
  `rpt_data_sistema` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_sistema`)),
  `rpt_data_component` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_component`)),
  `rpt_data_maquina` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_data_maquina`)),
  `rpt_valores_operaciones` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`rpt_valores_operaciones`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_rpt_frt`
--

CREATE TABLE `reports_rpt_frt` (
  `RptAr_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `formato_id` bigint(20) NOT NULL,
  `reporte_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_rpt_prt`
--

CREATE TABLE `reports_rpt_prt` (
  `RptPrt_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `formato_id` bigint(20) NOT NULL,
  `protocolo_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_rpt_prt`
--

INSERT INTO `reports_rpt_prt` (`RptPrt_id`, `created_at`, `formato_id`, `protocolo_id`) VALUES
(1, '2022-10-19 00:25:26.262209', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_rpt_secc`
--

CREATE TABLE `reports_rpt_secc` (
  `RptSecc_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `formato_id` bigint(20) NOT NULL,
  `seccion_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_rpt_secc`
--

INSERT INTO `reports_rpt_secc` (`RptSecc_id`, `created_at`, `formato_id`, `seccion_id`) VALUES
(1, '2022-10-19 00:25:26.264214', 1, 5),
(2, '2022-10-19 00:25:26.264214', 1, 1),
(3, '2022-10-19 00:25:26.265208', 1, 2),
(4, '2022-10-19 00:25:26.265208', 1, 3),
(5, '2022-10-19 00:25:26.265208', 1, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reports_sistemas_tubos`
--

CREATE TABLE `reports_sistemas_tubos` (
  `StmTb_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `sistema_id` bigint(20) NOT NULL,
  `tubo_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reports_sistemas_tubos`
--

INSERT INTO `reports_sistemas_tubos` (`StmTb_id`, `created_at`, `sistema_id`, `tubo_id`) VALUES
(1, '2022-10-19 11:18:44.341964', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tests_calculo_operacion`
--

CREATE TABLE `tests_calculo_operacion` (
  `PrbCalOpr_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `calculo_id` bigint(20) DEFAULT NULL,
  `operacion_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tests_calculo_operacion`
--

INSERT INTO `tests_calculo_operacion` (`PrbCalOpr_id`, `created_at`, `calculo_id`, `operacion_id`) VALUES
(1, '2022-10-18 20:23:09.114355', 1, 1),
(2, '2022-10-18 20:24:10.670323', 2, 2),
(3, '2022-10-18 20:26:37.544468', 3, 3),
(4, '2022-10-18 20:27:39.171062', 4, 4),
(5, '2022-10-18 20:29:24.452361', 5, 5),
(6, '2022-10-19 00:05:27.498015', 6, 6),
(7, '2022-10-19 00:06:11.911464', 7, 7),
(8, '2022-10-19 00:07:31.907307', 8, 8),
(9, '2022-10-19 00:08:27.838580', 9, 9),
(10, '2022-10-19 00:10:03.223006', 10, 10),
(11, '2022-10-19 00:11:36.719215', 11, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tests_pruebacalculo`
--

CREATE TABLE `tests_pruebacalculo` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `prb_cal_id` bigint(20) NOT NULL,
  `prb_cal_titulo` varchar(255) NOT NULL,
  `prb_cal_contexto` longtext DEFAULT NULL,
  `prb_cal_resultado` longtext DEFAULT NULL,
  `prb_cal_tolerancia` longtext NOT NULL,
  `prb_cal_condicion_respuesta` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`prb_cal_condicion_respuesta`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tests_pruebacalculo`
--

INSERT INTO `tests_pruebacalculo` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `prb_cal_id`, `prb_cal_titulo`, `prb_cal_contexto`, `prb_cal_resultado`, `prb_cal_tolerancia`, `prb_cal_condicion_respuesta`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'Alineación de rayos X / haz luminoso', '', '', 'Suma de las desviaciones en los bordes inferiores 2.0% de la distancia entre el foco y el maniquí de colimación para cada dirección principal. La suma total de las desviaciones no excederá el 3% de la distancia entre el foco y el maniquí de colimación.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 2, 'Ortogonalidad del haz de rayos X y del receptor de imagen', '', '', 'El ángulo que forman el eje central del haz de rayos X y el plano del receptor de imagen no deberá desviarse de los 90° más de 1.5°.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 3, 'Tamaño del campo de entrada del detector de imagen', '', '', 'Para campos circulares: DM/DN ≥ 0.85. Para campos rectangulares sustituir el diámetro por la diagonal media.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 4, 'Distorsión Geométrica', '', '', '≤ 10%', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 5, 'Coincidencia del campo de radiación con el área visualizada del detector', '', '', 'La relación entre el área del campo de radiación y el área visualizada en la superficie de entrada del detector de imagen debe ser ≤ 1.15', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 6, 'Exactitud de la tensión', '', '', 'Desviación con respecto al valor nominal < ±10%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 7, 'Repetibilidad de la tensión', '', '', 'Coeficiente de variación < 5%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 8, 'Filtración (Capa Hemirreductora)', '', '', '> 2.5 mmAl (a 70 kVp) y >2.9 mmAl (a 80 kVp)', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 9, 'Exactitud del tiempo de exposición', '', '', 'Desviación con respecto al valor nominal < ±10% para tiempos > 20 ms y lo especificado por el fabricante para tiempos ≤ 20 ms', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 10, 'Repetibilidad del tiempo de exposición', '', '', 'Coeficiente de variación < 10%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}'),
(1, '2022-10-18', '2022-10-18', '2022-10-18', 11, 'Repetibilidad del rendimiento', '', '', 'Coeficiente de variación < 10%.', '{\"true\": \"S\\u00cd\", \"false\": \"NO\"}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tests_pruebaopciones`
--

CREATE TABLE `tests_pruebaopciones` (
  `is_enabled` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `deleted_at` date NOT NULL,
  `prb_opc_id` bigint(20) NOT NULL,
  `prb_opc_titulo` varchar(255) NOT NULL,
  `prb_opc_contexto` longtext DEFAULT NULL,
  `prb_opc_resultado` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`prb_opc_resultado`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tests_pruebaopciones`
--

INSERT INTO `tests_pruebaopciones` (`is_enabled`, `created_at`, `updated_at`, `deleted_at`, `prb_opc_id`, `prb_opc_titulo`, `prb_opc_contexto`, `prb_opc_resultado`) VALUES
(1, '2022-10-18', '2022-10-18', '2022-10-18', 1, 'CARACTERISTICA', '', '[{\"opcion\": \"ESTABILIDAD MECANICA\"}, {\"opcion\": \"MOVIMIENTOS ADECUADOS DEL EQUIPO\"}, {\"opcion\": \"BUEN ESTADO DE LOS CABLES (ALTA TENSION Y ALIMENTACION)\"}, {\"opcion\": \"EXISTE INDICADOR DEL PUNTO FOCAL\"}, {\"opcion\": \"LOS INDICADORES DE TECNICA DE EXPOSICION EN EL PANEL DE CONTROL FUNCIONAN ADECUADAMENTE\"}, {\"opcion\": \"EXISTE SE\\u00d1AL AUDIBLE DURANTE Y/O AL FINAL DE LA EXPOSICION \"}, {\"opcion\": \"EXISTE INTERRUPTOR DE EXPOSICION TIPO HOMBRE MUERTO\"}, {\"opcion\": \"EXISTE INTERRUPTOR DE EXPOSICION TIPO PEDAL DE DISPARO\"}]');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tests_prueba_tipos`
--

CREATE TABLE `tests_prueba_tipos` (
  `PrbCal_id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `calculo_id` bigint(20) DEFAULT NULL,
  `opcion_id` bigint(20) DEFAULT NULL,
  `seccion_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tests_prueba_tipos`
--

INSERT INTO `tests_prueba_tipos` (`PrbCal_id`, `created_at`, `calculo_id`, `opcion_id`, `seccion_id`) VALUES
(1, '2022-10-18 20:29:53.682408', 1, NULL, 1),
(2, '2022-10-18 20:29:53.682408', 2, NULL, 1),
(3, '2022-10-18 20:29:53.683407', 3, NULL, 1),
(4, '2022-10-18 20:29:53.683407', 4, NULL, 1),
(5, '2022-10-18 20:29:53.683407', 5, NULL, 1),
(6, '2022-10-19 00:07:36.782701', 6, NULL, 2),
(7, '2022-10-19 00:07:36.782701', 7, NULL, 2),
(8, '2022-10-19 00:07:36.782701', 8, NULL, 2),
(9, '2022-10-19 00:10:07.300852', 9, NULL, 3),
(10, '2022-10-19 00:10:07.300852', 10, NULL, 3),
(11, '2022-10-19 00:12:09.821927', 11, NULL, 4),
(12, '2022-10-19 00:13:20.172366', NULL, 1, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `token_blacklist_blacklistedtoken`
--

CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint(20) NOT NULL,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `token_blacklist_outstandingtoken`
--

CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint(20) NOT NULL,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `jti` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `token_blacklist_outstandingtoken`
--

INSERT INTO `token_blacklist_outstandingtoken` (`id`, `token`, `created_at`, `expires_at`, `user_id`, `jti`) VALUES
(1, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjEyMTg3NCwiaWF0IjoxNjY2MTE0Njc0LCJqdGkiOiI3YmRjOTc0MGRiZDY0NTA4OTBkZTM2MWI2NDkwMjBjZSIsInVzZXJfaWQiOjF9.5NmWhdiGj1OvildZmTCgipyP7htI435HpSbOeHmD0sI', '2022-10-18 17:37:54.240563', '2022-10-18 19:37:54.000000', 1, '7bdc9740dbd6450890de361b649020ce'),
(2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjEzMTI5MiwiaWF0IjoxNjY2MTI0MDkyLCJqdGkiOiI2MDYzMmIzNmNmMjg0NDI4YjdlZDI5OTE3MWIwYmMzMSIsInVzZXJfaWQiOjF9.G3ScH3t7LjY1gnA7wc3ZsUJezrK07W1PAsug_itCLz0', '2022-10-18 20:14:52.609557', '2022-10-18 22:14:52.000000', 1, '60632b36cf284428b7ed299171b0bc31'),
(3, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE0NjIzOCwiaWF0IjoxNjY2MTM5MDM4LCJqdGkiOiI0MDIyYWY0MmM3MTQ0ZDM3YTA0NGI3YjRhMzAxZTQzYiIsInVzZXJfaWQiOjF9.s9r4VGDju3CBPSuw6cNKWrtE6ddLgpnt4uzHA4P7Ayg', '2022-10-19 00:23:58.442198', '2022-10-19 02:23:58.000000', 1, '4022af42c7144d37a044b7b4a301e43b'),
(4, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE0NjI0MywiaWF0IjoxNjY2MTM5MDQzLCJqdGkiOiI4MTYwYmFhYWM1MTE0MmI5OGViODgyYWFlNjE1MDg3MCIsInVzZXJfaWQiOjF9.EZ7l14vypJTUdCu46ARTDHTvrGCM9JCR5gnAwcHyNLA', '2022-10-19 00:24:03.124176', '2022-10-19 02:24:03.000000', 1, '8160baaac51142b98eb882aae6150870'),
(5, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE0NjI1NSwiaWF0IjoxNjY2MTM5MDU1LCJqdGkiOiI0MDY1NDNkOWI1NjA0ZmMzYTgzMDk4ZDEyNTYzYTFhNyIsInVzZXJfaWQiOjF9.4P_COc-KG0Cv2P7xBed3J1UvoPqq8VpIaEm2X70KGys', '2022-10-19 00:24:15.696796', '2022-10-19 02:24:15.000000', 1, '406543d9b5604fc3a83098d12563a1a7'),
(6, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE1MzU5NiwiaWF0IjoxNjY2MTQ2Mzk2LCJqdGkiOiIzNDkxZWExMWVjMjg0N2FmYTAyZDQ3MjEzOTBiOTlhOSIsInVzZXJfaWQiOjF9.oC5Tg9Ax6szEHAX6Rhwbf5ocaJ2ZUCfE5EdErQ4XoT8', '2022-10-19 02:26:36.183744', '2022-10-19 04:26:36.000000', 1, '3491ea11ec2847afa02d4721390b99a9'),
(7, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE2MTE4NCwiaWF0IjoxNjY2MTUzOTg0LCJqdGkiOiIyZTYzZTc2MzAyOGE0Y2YxYmVlM2U5ZjExZjRiNzE1NSIsInVzZXJfaWQiOjF9.qIJHhbLVBy5TR9VCJ5gXOwxcJARWI2X0D8ZL_EL6yPk', '2022-10-19 04:33:04.248786', '2022-10-19 06:33:04.000000', 1, '2e63e763028a4cf1bee3e9f11f4b7155'),
(8, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE2ODQxNiwiaWF0IjoxNjY2MTYxMjE2LCJqdGkiOiJmODcxNWU1NDg2OTQ0MDM4YmUzNDQxMGJjMDNlNTU2NyIsInVzZXJfaWQiOjF9.VT0l2jrOvsOovdlS3Q-uNFUNoJ9LpfG_CV9QpJUX9w8', '2022-10-19 06:33:36.718294', '2022-10-19 08:33:36.000000', 1, 'f8715e5486944038be34410bc03e5567'),
(9, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE4NDgxOCwiaWF0IjoxNjY2MTc3NjE4LCJqdGkiOiIzOGI0ZTRkMzdhYWQ0ZmFlOGY3Njg2NTAyNTEwNDY4MSIsInVzZXJfaWQiOjF9.uuRtRQsCRHjisL580104p_-jqnl4nCVkhe4H7AD-hNA', '2022-10-19 11:06:58.689565', '2022-10-19 13:06:58.000000', 1, '38b4e4d37aad4fae8f76865025104681'),
(10, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjE5MjEwMCwiaWF0IjoxNjY2MTg0OTAwLCJqdGkiOiI5ZWY5MTIwMmIzNmQ0NDcyOGJjZTNhODYyYjI2OTkxYSIsInVzZXJfaWQiOjF9.no340wer9bqDQzMZrt1F35d_8546N4KAJ67w5o3YBWQ', '2022-10-19 13:08:20.405734', '2022-10-19 15:08:20.000000', 1, '9ef91202b36d44728bce3a862b26991a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_historicaluser`
--

CREATE TABLE `user_historicaluser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `image` longtext DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user_historicaluser`
--

INSERT INTO `user_historicaluser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `email`, `name`, `last_name`, `image`, `is_active`, `is_staff`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, 'pbkdf2_sha256$390000$uq11k3dUi6LB7zniYxPS2N$EvPDJE2+mgs/itnAheomtH4X7Pm6MpASlKrWx/WkPpM=', NULL, 1, 'Programador', 'programacionaleph@gmail.com', 'Marcello ', 'Cano Lopez Torres', '', 1, 1, 1, '2022-10-18 15:41:31.848284', NULL, '+', NULL),
(1, 'pbkdf2_sha256$390000$uq11k3dUi6LB7zniYxPS2N$EvPDJE2+mgs/itnAheomtH4X7Pm6MpASlKrWx/WkPpM=', '2022-10-18 15:41:59.904420', 1, 'Programador', 'programacionaleph@gmail.com', 'Marcello ', 'Cano Lopez Torres', '', 1, 1, 2, '2022-10-18 15:41:59.906993', NULL, '~', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user`
--

CREATE TABLE `user_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user_user`
--

INSERT INTO `user_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `email`, `name`, `last_name`, `image`, `is_active`, `is_staff`) VALUES
(1, 'pbkdf2_sha256$390000$uq11k3dUi6LB7zniYxPS2N$EvPDJE2+mgs/itnAheomtH4X7Pm6MpASlKrWx/WkPpM=', '2022-10-18 15:41:59.904420', 1, 'Programador', 'programacionaleph@gmail.com', 'Marcello ', 'Cano Lopez Torres', '', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user_groups`
--

CREATE TABLE `user_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user_user_permissions`
--

CREATE TABLE `user_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `categoria_operaciones`
--
ALTER TABLE `categoria_operaciones`
  ADD PRIMARY KEY (`CatOpr_id`),
  ADD KEY `categoria_operacione_categoria_id_c46dcacc_fk_operation` (`categoria_id`),
  ADD KEY `categoria_operacione_operacion_id_387dfee2_fk_operation` (`operacion_id`);

--
-- Indices de la tabla `companymachine_calibraciones`
--
ALTER TABLE `companymachine_calibraciones`
  ADD PRIMARY KEY (`cal_id`);

--
-- Indices de la tabla `companymachine_calibraciones_medidores`
--
ALTER TABLE `companymachine_calibraciones_medidores`
  ADD PRIMARY KEY (`CalMed_id`),
  ADD KEY `companymachine_calib_calibracion_id_dbf2c331_fk_companyma` (`calibracion_id`),
  ADD KEY `companymachine_calib_medidor_id_c418343e_fk_companyma` (`medidor_id`);

--
-- Indices de la tabla `companymachine_historicalcalibracionesmodel`
--
ALTER TABLE `companymachine_historicalcalibracionesmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `CompanyMachine_historicalcalibracionesmodel_cal_id_42d82876` (`cal_id`),
  ADD KEY `CompanyMachine_histo_history_user_id_49ef41d1_fk_User_user` (`history_user_id`),
  ADD KEY `CompanyMachine_historicalca_history_date_03f0a929` (`history_date`);

--
-- Indices de la tabla `companymachine_historicalmedidoresmodel`
--
ALTER TABLE `companymachine_historicalmedidoresmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `CompanyMachine_historicalmedidoresmodel_med_id_f23696fd` (`med_id`),
  ADD KEY `CompanyMachine_historicalme_med_serie_medidor_16ce94bc` (`med_serie_medidor`),
  ADD KEY `CompanyMachine_histo_history_user_id_44e3e24a_fk_User_user` (`history_user_id`),
  ADD KEY `CompanyMachine_historicalmedidoresmodel_history_date_4c187178` (`history_date`);

--
-- Indices de la tabla `companymachine_medidores`
--
ALTER TABLE `companymachine_medidores`
  ADD PRIMARY KEY (`med_id`),
  ADD UNIQUE KEY `med_serie_medidor` (`med_serie_medidor`);

--
-- Indices de la tabla `customers_ambientes`
--
ALTER TABLE `customers_ambientes`
  ADD PRIMARY KEY (`ar_id`);

--
-- Indices de la tabla `customers_contactos`
--
ALTER TABLE `customers_contactos`
  ADD PRIMARY KEY (`con_id`);

--
-- Indices de la tabla `customers_contactos_departamento`
--
ALTER TABLE `customers_contactos_departamento`
  ADD PRIMARY KEY (`ConDpt_id`),
  ADD KEY `customers_contactos__contacto_id_2e95b660_fk_customers` (`contacto_id`),
  ADD KEY `customers_contactos__departamento_id_5a7b293a_fk_customers` (`departamento_id`);

--
-- Indices de la tabla `customers_departamento_ambiente`
--
ALTER TABLE `customers_departamento_ambiente`
  ADD PRIMARY KEY (`ArDpt_id`),
  ADD KEY `customers_departamen_area_id_c3131e5a_fk_customers` (`area_id`),
  ADD KEY `customers_departamen_departamento_id_f4337c3d_fk_customers` (`departamento_id`);

--
-- Indices de la tabla `customers_depatamentos`
--
ALTER TABLE `customers_depatamentos`
  ADD PRIMARY KEY (`dpt_id`);

--
-- Indices de la tabla `customers_organizaciones`
--
ALTER TABLE `customers_organizaciones`
  ADD PRIMARY KEY (`org_id`),
  ADD UNIQUE KEY `org_razon_social` (`org_razon_social`),
  ADD UNIQUE KEY `org_ruc` (`org_ruc`),
  ADD UNIQUE KEY `org_nombre_comercial` (`org_nombre_comercial`);

--
-- Indices de la tabla `customers_organizacion_departamentos`
--
ALTER TABLE `customers_organizacion_departamentos`
  ADD PRIMARY KEY (`DptOrg_id`),
  ADD KEY `customers_organizaci_departamento_id_2cc1aefd_fk_customers` (`departamento_id`),
  ADD KEY `customers_organizaci_organizacion_id_5a01b954_fk_customers` (`organizacion_id`);

--
-- Indices de la tabla `customer_historicalareasmodel`
--
ALTER TABLE `customer_historicalareasmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Customer_historicalareasmodel_ar_id_0536a713` (`ar_id`),
  ADD KEY `Customer_historicala_history_user_id_596bb82d_fk_User_user` (`history_user_id`),
  ADD KEY `Customer_historicalareasmodel_history_date_56ce5fe2` (`history_date`);

--
-- Indices de la tabla `customer_historicalcontactosmodel`
--
ALTER TABLE `customer_historicalcontactosmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Customer_historicalcontactosmodel_con_id_de650c7f` (`con_id`),
  ADD KEY `Customer_historicalc_history_user_id_4e21e027_fk_User_user` (`history_user_id`),
  ADD KEY `Customer_historicalcontactosmodel_history_date_d3287fc5` (`history_date`);

--
-- Indices de la tabla `customer_historicaldepartamentomodel`
--
ALTER TABLE `customer_historicaldepartamentomodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Customer_historicaldepartamentomodel_dpt_id_85cf2af7` (`dpt_id`),
  ADD KEY `Customer_historicald_history_user_id_01f3ad93_fk_User_user` (`history_user_id`),
  ADD KEY `Customer_historicaldepartamentomodel_history_date_ddfcb3e0` (`history_date`);

--
-- Indices de la tabla `customer_historicalorganizacionmodel`
--
ALTER TABLE `customer_historicalorganizacionmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Customer_historicalorganizacionmodel_org_id_51f6ef0d` (`org_id`),
  ADD KEY `Customer_historicalorganizacionmodel_org_ruc_21b9e375` (`org_ruc`),
  ADD KEY `Customer_historicalorganizacionmodel_org_razon_social_1ff12359` (`org_razon_social`),
  ADD KEY `Customer_historicalorganiza_org_nombre_comercial_956b32cf` (`org_nombre_comercial`),
  ADD KEY `Customer_historicalo_history_user_id_7df32869_fk_User_user` (`history_user_id`),
  ADD KEY `Customer_historicalorganizacionmodel_history_date_a2afbd7b` (`history_date`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_User_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `machines_sistemas`
--
ALTER TABLE `machines_sistemas`
  ADD PRIMARY KEY (`stm_id`),
  ADD UNIQUE KEY `stm_serie_sistema` (`stm_serie_sistema`);

--
-- Indices de la tabla `machines_tubos`
--
ALTER TABLE `machines_tubos`
  ADD PRIMARY KEY (`tb_id`),
  ADD UNIQUE KEY `tb_serie_componente` (`tb_serie_componente`);

--
-- Indices de la tabla `machine_historicalsistemamodel`
--
ALTER TABLE `machine_historicalsistemamodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Machine_historicalsi_history_user_id_ea75b5f4_fk_User_user` (`history_user_id`),
  ADD KEY `Machine_historicalsistemamodel_stm_id_be12e348` (`stm_id`),
  ADD KEY `Machine_historicalsistemamodel_stm_serie_sistema_3c255100` (`stm_serie_sistema`),
  ADD KEY `Machine_historicalsistemamodel_history_date_e209ef22` (`history_date`);

--
-- Indices de la tabla `machine_historicaltubomodel`
--
ALTER TABLE `machine_historicaltubomodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Machine_historicaltu_history_user_id_ceac0b40_fk_User_user` (`history_user_id`),
  ADD KEY `Machine_historicaltubomodel_tb_id_9e1f9fef` (`tb_id`),
  ADD KEY `Machine_historicaltubomodel_tb_serie_componente_56b825a9` (`tb_serie_componente`),
  ADD KEY `Machine_historicaltubomodel_history_date_59b52b52` (`history_date`);

--
-- Indices de la tabla `operacion_variables`
--
ALTER TABLE `operacion_variables`
  ADD PRIMARY KEY (`OprVar_id`),
  ADD KEY `operacion_variables_operacion_id_5799c910_fk_operation` (`operacion_id`),
  ADD KEY `operacion_variables_variables_id_42460608_fk_operation` (`variables_id`);

--
-- Indices de la tabla `operations_categorias_operaciones`
--
ALTER TABLE `operations_categorias_operaciones`
  ADD PRIMARY KEY (`cat_opr_id`);

--
-- Indices de la tabla `operations_historicalcategoryoperacionesmodel`
--
ALTER TABLE `operations_historicalcategoryoperacionesmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Operations_historica_history_user_id_9bffef2d_fk_User_user` (`history_user_id`),
  ADD KEY `Operations_historicalcatego_cat_opr_id_499e9c79` (`cat_opr_id`),
  ADD KEY `Operations_historicalcatego_history_date_fff16753` (`history_date`);

--
-- Indices de la tabla `operations_historicaloperacionesmodel`
--
ALTER TABLE `operations_historicaloperacionesmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Operations_historica_history_user_id_f74d7d36_fk_User_user` (`history_user_id`),
  ADD KEY `Operations_historicaloperacionesmodel_opr_id_726204f8` (`opr_id`),
  ADD KEY `Operations_historicaloperacionesmodel_opr_titulo_b62f83a5` (`opr_titulo`),
  ADD KEY `Operations_historicaloperacionesmodel_opr_funcion_d830cc0b` (`opr_funcion`),
  ADD KEY `Operations_historicaloperacionesmodel_opr_simbolo_821c05c3` (`opr_simbolo`),
  ADD KEY `Operations_historicaloperacionesmodel_history_date_0bc4e9c1` (`history_date`);

--
-- Indices de la tabla `operations_historicalvariablesmodel`
--
ALTER TABLE `operations_historicalvariablesmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Operations_historica_history_user_id_00c5ce59_fk_User_user` (`history_user_id`),
  ADD KEY `Operations_historicalvariablesmodel_var_id_11ab155f` (`var_id`),
  ADD KEY `Operations_historicalvariablesmodel_history_date_1c6cc762` (`history_date`),
  ADD KEY `Operations_historicalvariablesmodel_var_nombre_d21e1f8e` (`var_nombre`);

--
-- Indices de la tabla `operations_operaciones`
--
ALTER TABLE `operations_operaciones`
  ADD PRIMARY KEY (`opr_id`),
  ADD UNIQUE KEY `opr_titulo` (`opr_titulo`),
  ADD UNIQUE KEY `opr_funcion` (`opr_funcion`),
  ADD UNIQUE KEY `opr_simbolo` (`opr_simbolo`);

--
-- Indices de la tabla `operations_variables`
--
ALTER TABLE `operations_variables`
  ADD PRIMARY KEY (`var_id`),
  ADD UNIQUE KEY `operations_Variables_var_nombre_75dfa319_uniq` (`var_nombre`);

--
-- Indices de la tabla `protocols_protocolos`
--
ALTER TABLE `protocols_protocolos`
  ADD PRIMARY KEY (`prt_id`),
  ADD UNIQUE KEY `prt_nombre` (`prt_nombre`);

--
-- Indices de la tabla `protocols_protocolo_secciones`
--
ALTER TABLE `protocols_protocolo_secciones`
  ADD PRIMARY KEY (`PrtScc_id`),
  ADD KEY `protocols_protocolo__protocolo_id_f7780003_fk_protocols` (`protocolo_id`),
  ADD KEY `protocols_protocolo__seccion_id_2fc17189_fk_protocols` (`seccion_id`);

--
-- Indices de la tabla `protocols_secciones`
--
ALTER TABLE `protocols_secciones`
  ADD PRIMARY KEY (`scc_id`),
  ADD UNIQUE KEY `scc_nombre` (`scc_nombre`);

--
-- Indices de la tabla `protocol_historicalprotocolsmodel`
--
ALTER TABLE `protocol_historicalprotocolsmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Protocol_historicalp_history_user_id_a1a9d173_fk_User_user` (`history_user_id`),
  ADD KEY `Protocol_historicalprotocolsmodel_prt_id_b0d81c7e` (`prt_id`),
  ADD KEY `Protocol_historicalprotocolsmodel_prt_nombre_b24eec76` (`prt_nombre`),
  ADD KEY `Protocol_historicalprotocolsmodel_history_date_7a43b29e` (`history_date`);

--
-- Indices de la tabla `protocol_historicalpruebacalculomodel`
--
ALTER TABLE `protocol_historicalpruebacalculomodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Protocol_historicalp_history_user_id_f06cfc0b_fk_User_user` (`history_user_id`),
  ADD KEY `Protocol_historicalpruebacalculomodel_prb_cal_id_8fb6dd04` (`prb_cal_id`),
  ADD KEY `Protocol_historicalpruebacalculomodel_prb_cal_titulo_bcf3d4b1` (`prb_cal_titulo`),
  ADD KEY `Protocol_historicalpruebacalculomodel_history_date_997223e7` (`history_date`);

--
-- Indices de la tabla `protocol_historicalpruebaopcionesmodel`
--
ALTER TABLE `protocol_historicalpruebaopcionesmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Protocol_historicalp_history_user_id_74f8bfe6_fk_User_user` (`history_user_id`),
  ADD KEY `Protocol_historicalpruebaopcionesmodel_prb_opc_id_d9db68e5` (`prb_opc_id`),
  ADD KEY `Protocol_historicalpruebaopcionesmodel_prb_opc_titulo_5e981484` (`prb_opc_titulo`),
  ADD KEY `Protocol_historicalpruebaopcionesmodel_history_date_08daa076` (`history_date`);

--
-- Indices de la tabla `protocol_historicalseccionesmodel`
--
ALTER TABLE `protocol_historicalseccionesmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Protocol_historicals_history_user_id_4f5b73a3_fk_User_user` (`history_user_id`),
  ADD KEY `Protocol_historicalseccionesmodel_scc_id_f796559d` (`scc_id`),
  ADD KEY `Protocol_historicalseccionesmodel_scc_nombre_7a82223e` (`scc_nombre`),
  ADD KEY `Protocol_historicalseccionesmodel_history_date_fd8cfd03` (`history_date`);

--
-- Indices de la tabla `reports_categorias`
--
ALTER TABLE `reports_categorias`
  ADD PRIMARY KEY (`rep_cat_id`),
  ADD UNIQUE KEY `rep_cat_abreviatura` (`rep_cat_abreviatura`);

--
-- Indices de la tabla `reports_formatos`
--
ALTER TABLE `reports_formatos`
  ADD PRIMARY KEY (`rep_frt_id`),
  ADD UNIQUE KEY `rep_frt_codigo` (`rep_frt_codigo`);

--
-- Indices de la tabla `reports_formatos_categoria`
--
ALTER TABLE `reports_formatos_categoria`
  ADD PRIMARY KEY (`FrtCat_id`),
  ADD KEY `reports_formatos_cat_categoria_id_73f1cc44_fk_reports_C` (`categoria_id`),
  ADD KEY `reports_formatos_cat_formatos_id_ae08995b_fk_reports_F` (`formatos_id`);

--
-- Indices de la tabla `reports_historicalreportscategorymodel`
--
ALTER TABLE `reports_historicalreportscategorymodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Reports_historicalre_history_user_id_51ed426f_fk_User_user` (`history_user_id`),
  ADD KEY `Reports_historicalreportscategorymodel_rep_cat_id_ccf45040` (`rep_cat_id`),
  ADD KEY `Reports_historicalreportsca_rep_cat_abreviatura_86c4138c` (`rep_cat_abreviatura`),
  ADD KEY `Reports_historicalreportscategorymodel_history_date_0a2e8f97` (`history_date`);

--
-- Indices de la tabla `reports_historicalreportsformatsmodel`
--
ALTER TABLE `reports_historicalreportsformatsmodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Reports_historicalre_history_user_id_8c85e68a_fk_User_user` (`history_user_id`),
  ADD KEY `Reports_historicalreportsformatsmodel_rep_frt_id_0963ee2c` (`rep_frt_id`),
  ADD KEY `Reports_historicalreportsformatsmodel_rep_frt_codigo_ebe8e2d1` (`rep_frt_codigo`),
  ADD KEY `Reports_historicalreportsformatsmodel_history_date_442d7648` (`history_date`);

--
-- Indices de la tabla `reports_historicalreportsreportemodel`
--
ALTER TABLE `reports_historicalreportsreportemodel`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `Reports_historicalre_history_user_id_dd59a956_fk_User_user` (`history_user_id`),
  ADD KEY `Reports_historicalreportsreportemodel_rpt_id_c3b6eb8d` (`rpt_id`),
  ADD KEY `Reports_historicalreportsreportemodel_history_date_a6858096` (`history_date`);

--
-- Indices de la tabla `reports_reportes`
--
ALTER TABLE `reports_reportes`
  ADD PRIMARY KEY (`rpt_id`);

--
-- Indices de la tabla `reports_rpt_frt`
--
ALTER TABLE `reports_rpt_frt`
  ADD PRIMARY KEY (`RptAr_id`),
  ADD KEY `reports_rpt_Frt_formato_id_5c8b29f5_fk_reports_F` (`formato_id`),
  ADD KEY `reports_rpt_Frt_reporte_id_044898e1_fk_reports_Reportes_rpt_id` (`reporte_id`);

--
-- Indices de la tabla `reports_rpt_prt`
--
ALTER TABLE `reports_rpt_prt`
  ADD PRIMARY KEY (`RptPrt_id`),
  ADD KEY `reports_rpt_Prt_formato_id_8c46a6c2_fk_reports_F` (`formato_id`),
  ADD KEY `reports_rpt_Prt_protocolo_id_84e57670_fk_protocols` (`protocolo_id`);

--
-- Indices de la tabla `reports_rpt_secc`
--
ALTER TABLE `reports_rpt_secc`
  ADD PRIMARY KEY (`RptSecc_id`),
  ADD KEY `reports_rpt_secc_formato_id_dd2e34a5_fk_reports_F` (`formato_id`),
  ADD KEY `reports_rpt_secc_seccion_id_d48bd7e4_fk_protocols` (`seccion_id`);

--
-- Indices de la tabla `reports_sistemas_tubos`
--
ALTER TABLE `reports_sistemas_tubos`
  ADD PRIMARY KEY (`StmTb_id`),
  ADD KEY `reports_sistemas_tub_sistema_id_0cb88b7c_fk_machines_` (`sistema_id`),
  ADD KEY `reports_sistemas_tubos_tubo_id_12e032cf_fk_machines_Tubos_tb_id` (`tubo_id`);

--
-- Indices de la tabla `tests_calculo_operacion`
--
ALTER TABLE `tests_calculo_operacion`
  ADD PRIMARY KEY (`PrbCalOpr_id`),
  ADD KEY `tests_calculo_operac_calculo_id_4d540543_fk_tests_Pru` (`calculo_id`),
  ADD KEY `tests_calculo_operac_operacion_id_763579b7_fk_operation` (`operacion_id`);

--
-- Indices de la tabla `tests_pruebacalculo`
--
ALTER TABLE `tests_pruebacalculo`
  ADD PRIMARY KEY (`prb_cal_id`),
  ADD UNIQUE KEY `prb_cal_titulo` (`prb_cal_titulo`);

--
-- Indices de la tabla `tests_pruebaopciones`
--
ALTER TABLE `tests_pruebaopciones`
  ADD PRIMARY KEY (`prb_opc_id`),
  ADD UNIQUE KEY `prb_opc_titulo` (`prb_opc_titulo`);

--
-- Indices de la tabla `tests_prueba_tipos`
--
ALTER TABLE `tests_prueba_tipos`
  ADD PRIMARY KEY (`PrbCal_id`),
  ADD KEY `tests_prueba_tipos_calculo_id_97cc5014_fk_tests_Pru` (`calculo_id`),
  ADD KEY `tests_prueba_tipos_opcion_id_19c87f70_fk_tests_Pru` (`opcion_id`),
  ADD KEY `tests_prueba_tipos_seccion_id_a760d3c4_fk_protocols` (`seccion_id`);

--
-- Indices de la tabla `token_blacklist_blacklistedtoken`
--
ALTER TABLE `token_blacklist_blacklistedtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token_id` (`token_id`);

--
-- Indices de la tabla `token_blacklist_outstandingtoken`
--
ALTER TABLE `token_blacklist_outstandingtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  ADD KEY `token_blacklist_outs_user_id_83bc629a_fk_User_user` (`user_id`);

--
-- Indices de la tabla `user_historicaluser`
--
ALTER TABLE `user_historicaluser`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `User_historicaluser_history_user_id_99619363_fk_User_user_id` (`history_user_id`),
  ADD KEY `User_historicaluser_id_63ee20f1` (`id`),
  ADD KEY `User_historicaluser_username_d84136ac` (`username`),
  ADD KEY `User_historicaluser_email_e0a63685` (`email`),
  ADD KEY `User_historicaluser_history_date_5be247f9` (`history_date`);

--
-- Indices de la tabla `user_user`
--
ALTER TABLE `user_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `User_user_groups_user_id_group_id_e1236af7_uniq` (`user_id`,`group_id`),
  ADD KEY `User_user_groups_group_id_ca46cfeb_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `User_user_user_permissions_user_id_permission_id_f20e58ff_uniq` (`user_id`,`permission_id`),
  ADD KEY `User_user_user_permi_permission_id_6ee76041_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=241;

--
-- AUTO_INCREMENT de la tabla `categoria_operaciones`
--
ALTER TABLE `categoria_operaciones`
  MODIFY `CatOpr_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `companymachine_calibraciones`
--
ALTER TABLE `companymachine_calibraciones`
  MODIFY `cal_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `companymachine_calibraciones_medidores`
--
ALTER TABLE `companymachine_calibraciones_medidores`
  MODIFY `CalMed_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `companymachine_historicalcalibracionesmodel`
--
ALTER TABLE `companymachine_historicalcalibracionesmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `companymachine_historicalmedidoresmodel`
--
ALTER TABLE `companymachine_historicalmedidoresmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `companymachine_medidores`
--
ALTER TABLE `companymachine_medidores`
  MODIFY `med_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customers_ambientes`
--
ALTER TABLE `customers_ambientes`
  MODIFY `ar_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customers_contactos`
--
ALTER TABLE `customers_contactos`
  MODIFY `con_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customers_contactos_departamento`
--
ALTER TABLE `customers_contactos_departamento`
  MODIFY `ConDpt_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customers_departamento_ambiente`
--
ALTER TABLE `customers_departamento_ambiente`
  MODIFY `ArDpt_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `customers_depatamentos`
--
ALTER TABLE `customers_depatamentos`
  MODIFY `dpt_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customers_organizaciones`
--
ALTER TABLE `customers_organizaciones`
  MODIFY `org_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customers_organizacion_departamentos`
--
ALTER TABLE `customers_organizacion_departamentos`
  MODIFY `DptOrg_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customer_historicalareasmodel`
--
ALTER TABLE `customer_historicalareasmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `customer_historicalcontactosmodel`
--
ALTER TABLE `customer_historicalcontactosmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customer_historicaldepartamentomodel`
--
ALTER TABLE `customer_historicaldepartamentomodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `customer_historicalorganizacionmodel`
--
ALTER TABLE `customer_historicalorganizacionmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT de la tabla `machines_sistemas`
--
ALTER TABLE `machines_sistemas`
  MODIFY `stm_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `machines_tubos`
--
ALTER TABLE `machines_tubos`
  MODIFY `tb_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `machine_historicalsistemamodel`
--
ALTER TABLE `machine_historicalsistemamodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `machine_historicaltubomodel`
--
ALTER TABLE `machine_historicaltubomodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `operacion_variables`
--
ALTER TABLE `operacion_variables`
  MODIFY `OprVar_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `operations_categorias_operaciones`
--
ALTER TABLE `operations_categorias_operaciones`
  MODIFY `cat_opr_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `operations_historicalcategoryoperacionesmodel`
--
ALTER TABLE `operations_historicalcategoryoperacionesmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `operations_historicaloperacionesmodel`
--
ALTER TABLE `operations_historicaloperacionesmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `operations_historicalvariablesmodel`
--
ALTER TABLE `operations_historicalvariablesmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `operations_operaciones`
--
ALTER TABLE `operations_operaciones`
  MODIFY `opr_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `operations_variables`
--
ALTER TABLE `operations_variables`
  MODIFY `var_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `protocols_protocolos`
--
ALTER TABLE `protocols_protocolos`
  MODIFY `prt_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `protocols_protocolo_secciones`
--
ALTER TABLE `protocols_protocolo_secciones`
  MODIFY `PrtScc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `protocols_secciones`
--
ALTER TABLE `protocols_secciones`
  MODIFY `scc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `protocol_historicalprotocolsmodel`
--
ALTER TABLE `protocol_historicalprotocolsmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `protocol_historicalpruebacalculomodel`
--
ALTER TABLE `protocol_historicalpruebacalculomodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `protocol_historicalpruebaopcionesmodel`
--
ALTER TABLE `protocol_historicalpruebaopcionesmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `protocol_historicalseccionesmodel`
--
ALTER TABLE `protocol_historicalseccionesmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `reports_categorias`
--
ALTER TABLE `reports_categorias`
  MODIFY `rep_cat_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `reports_formatos`
--
ALTER TABLE `reports_formatos`
  MODIFY `rep_frt_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `reports_formatos_categoria`
--
ALTER TABLE `reports_formatos_categoria`
  MODIFY `FrtCat_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `reports_historicalreportscategorymodel`
--
ALTER TABLE `reports_historicalreportscategorymodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `reports_historicalreportsformatsmodel`
--
ALTER TABLE `reports_historicalreportsformatsmodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `reports_historicalreportsreportemodel`
--
ALTER TABLE `reports_historicalreportsreportemodel`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reports_reportes`
--
ALTER TABLE `reports_reportes`
  MODIFY `rpt_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reports_rpt_frt`
--
ALTER TABLE `reports_rpt_frt`
  MODIFY `RptAr_id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reports_rpt_prt`
--
ALTER TABLE `reports_rpt_prt`
  MODIFY `RptPrt_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `reports_rpt_secc`
--
ALTER TABLE `reports_rpt_secc`
  MODIFY `RptSecc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `reports_sistemas_tubos`
--
ALTER TABLE `reports_sistemas_tubos`
  MODIFY `StmTb_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tests_calculo_operacion`
--
ALTER TABLE `tests_calculo_operacion`
  MODIFY `PrbCalOpr_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `tests_pruebacalculo`
--
ALTER TABLE `tests_pruebacalculo`
  MODIFY `prb_cal_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `tests_pruebaopciones`
--
ALTER TABLE `tests_pruebaopciones`
  MODIFY `prb_opc_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tests_prueba_tipos`
--
ALTER TABLE `tests_prueba_tipos`
  MODIFY `PrbCal_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `token_blacklist_blacklistedtoken`
--
ALTER TABLE `token_blacklist_blacklistedtoken`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `token_blacklist_outstandingtoken`
--
ALTER TABLE `token_blacklist_outstandingtoken`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `user_historicaluser`
--
ALTER TABLE `user_historicaluser`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `user_user`
--
ALTER TABLE `user_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `categoria_operaciones`
--
ALTER TABLE `categoria_operaciones`
  ADD CONSTRAINT `categoria_operacione_categoria_id_c46dcacc_fk_operation` FOREIGN KEY (`categoria_id`) REFERENCES `operations_categorias_operaciones` (`cat_opr_id`),
  ADD CONSTRAINT `categoria_operacione_operacion_id_387dfee2_fk_operation` FOREIGN KEY (`operacion_id`) REFERENCES `operations_operaciones` (`opr_id`);

--
-- Filtros para la tabla `companymachine_calibraciones_medidores`
--
ALTER TABLE `companymachine_calibraciones_medidores`
  ADD CONSTRAINT `companymachine_calib_calibracion_id_dbf2c331_fk_companyma` FOREIGN KEY (`calibracion_id`) REFERENCES `companymachine_calibraciones` (`cal_id`),
  ADD CONSTRAINT `companymachine_calib_medidor_id_c418343e_fk_companyma` FOREIGN KEY (`medidor_id`) REFERENCES `companymachine_medidores` (`med_id`);

--
-- Filtros para la tabla `companymachine_historicalcalibracionesmodel`
--
ALTER TABLE `companymachine_historicalcalibracionesmodel`
  ADD CONSTRAINT `CompanyMachine_histo_history_user_id_49ef41d1_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `companymachine_historicalmedidoresmodel`
--
ALTER TABLE `companymachine_historicalmedidoresmodel`
  ADD CONSTRAINT `CompanyMachine_histo_history_user_id_44e3e24a_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `customers_contactos_departamento`
--
ALTER TABLE `customers_contactos_departamento`
  ADD CONSTRAINT `customers_contactos__contacto_id_2e95b660_fk_customers` FOREIGN KEY (`contacto_id`) REFERENCES `customers_contactos` (`con_id`),
  ADD CONSTRAINT `customers_contactos__departamento_id_5a7b293a_fk_customers` FOREIGN KEY (`departamento_id`) REFERENCES `customers_depatamentos` (`dpt_id`);

--
-- Filtros para la tabla `customers_departamento_ambiente`
--
ALTER TABLE `customers_departamento_ambiente`
  ADD CONSTRAINT `customers_departamen_area_id_c3131e5a_fk_customers` FOREIGN KEY (`area_id`) REFERENCES `customers_ambientes` (`ar_id`),
  ADD CONSTRAINT `customers_departamen_departamento_id_f4337c3d_fk_customers` FOREIGN KEY (`departamento_id`) REFERENCES `customers_depatamentos` (`dpt_id`);

--
-- Filtros para la tabla `customers_organizacion_departamentos`
--
ALTER TABLE `customers_organizacion_departamentos`
  ADD CONSTRAINT `customers_organizaci_departamento_id_2cc1aefd_fk_customers` FOREIGN KEY (`departamento_id`) REFERENCES `customers_depatamentos` (`dpt_id`),
  ADD CONSTRAINT `customers_organizaci_organizacion_id_5a01b954_fk_customers` FOREIGN KEY (`organizacion_id`) REFERENCES `customers_organizaciones` (`org_id`);

--
-- Filtros para la tabla `customer_historicalareasmodel`
--
ALTER TABLE `customer_historicalareasmodel`
  ADD CONSTRAINT `Customer_historicala_history_user_id_596bb82d_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `customer_historicalcontactosmodel`
--
ALTER TABLE `customer_historicalcontactosmodel`
  ADD CONSTRAINT `Customer_historicalc_history_user_id_4e21e027_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `customer_historicaldepartamentomodel`
--
ALTER TABLE `customer_historicaldepartamentomodel`
  ADD CONSTRAINT `Customer_historicald_history_user_id_01f3ad93_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `customer_historicalorganizacionmodel`
--
ALTER TABLE `customer_historicalorganizacionmodel`
  ADD CONSTRAINT `Customer_historicalo_history_user_id_7df32869_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `machine_historicalsistemamodel`
--
ALTER TABLE `machine_historicalsistemamodel`
  ADD CONSTRAINT `Machine_historicalsi_history_user_id_ea75b5f4_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `machine_historicaltubomodel`
--
ALTER TABLE `machine_historicaltubomodel`
  ADD CONSTRAINT `Machine_historicaltu_history_user_id_ceac0b40_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `operacion_variables`
--
ALTER TABLE `operacion_variables`
  ADD CONSTRAINT `operacion_variables_operacion_id_5799c910_fk_operation` FOREIGN KEY (`operacion_id`) REFERENCES `operations_operaciones` (`opr_id`),
  ADD CONSTRAINT `operacion_variables_variables_id_42460608_fk_operation` FOREIGN KEY (`variables_id`) REFERENCES `operations_variables` (`var_id`);

--
-- Filtros para la tabla `operations_historicalcategoryoperacionesmodel`
--
ALTER TABLE `operations_historicalcategoryoperacionesmodel`
  ADD CONSTRAINT `Operations_historica_history_user_id_9bffef2d_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `operations_historicaloperacionesmodel`
--
ALTER TABLE `operations_historicaloperacionesmodel`
  ADD CONSTRAINT `Operations_historica_history_user_id_f74d7d36_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `operations_historicalvariablesmodel`
--
ALTER TABLE `operations_historicalvariablesmodel`
  ADD CONSTRAINT `Operations_historica_history_user_id_00c5ce59_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `protocols_protocolo_secciones`
--
ALTER TABLE `protocols_protocolo_secciones`
  ADD CONSTRAINT `protocols_protocolo__protocolo_id_f7780003_fk_protocols` FOREIGN KEY (`protocolo_id`) REFERENCES `protocols_protocolos` (`prt_id`),
  ADD CONSTRAINT `protocols_protocolo__seccion_id_2fc17189_fk_protocols` FOREIGN KEY (`seccion_id`) REFERENCES `protocols_secciones` (`scc_id`);

--
-- Filtros para la tabla `protocol_historicalprotocolsmodel`
--
ALTER TABLE `protocol_historicalprotocolsmodel`
  ADD CONSTRAINT `Protocol_historicalp_history_user_id_a1a9d173_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `protocol_historicalpruebacalculomodel`
--
ALTER TABLE `protocol_historicalpruebacalculomodel`
  ADD CONSTRAINT `Protocol_historicalp_history_user_id_f06cfc0b_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `protocol_historicalpruebaopcionesmodel`
--
ALTER TABLE `protocol_historicalpruebaopcionesmodel`
  ADD CONSTRAINT `Protocol_historicalp_history_user_id_74f8bfe6_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `protocol_historicalseccionesmodel`
--
ALTER TABLE `protocol_historicalseccionesmodel`
  ADD CONSTRAINT `Protocol_historicals_history_user_id_4f5b73a3_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `reports_formatos_categoria`
--
ALTER TABLE `reports_formatos_categoria`
  ADD CONSTRAINT `reports_formatos_cat_categoria_id_73f1cc44_fk_reports_C` FOREIGN KEY (`categoria_id`) REFERENCES `reports_categorias` (`rep_cat_id`),
  ADD CONSTRAINT `reports_formatos_cat_formatos_id_ae08995b_fk_reports_F` FOREIGN KEY (`formatos_id`) REFERENCES `reports_formatos` (`rep_frt_id`);

--
-- Filtros para la tabla `reports_historicalreportscategorymodel`
--
ALTER TABLE `reports_historicalreportscategorymodel`
  ADD CONSTRAINT `Reports_historicalre_history_user_id_51ed426f_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `reports_historicalreportsformatsmodel`
--
ALTER TABLE `reports_historicalreportsformatsmodel`
  ADD CONSTRAINT `Reports_historicalre_history_user_id_8c85e68a_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `reports_historicalreportsreportemodel`
--
ALTER TABLE `reports_historicalreportsreportemodel`
  ADD CONSTRAINT `Reports_historicalre_history_user_id_dd59a956_fk_User_user` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `reports_rpt_frt`
--
ALTER TABLE `reports_rpt_frt`
  ADD CONSTRAINT `reports_rpt_Frt_formato_id_5c8b29f5_fk_reports_F` FOREIGN KEY (`formato_id`) REFERENCES `reports_formatos` (`rep_frt_id`),
  ADD CONSTRAINT `reports_rpt_Frt_reporte_id_044898e1_fk_reports_Reportes_rpt_id` FOREIGN KEY (`reporte_id`) REFERENCES `reports_reportes` (`rpt_id`);

--
-- Filtros para la tabla `reports_rpt_prt`
--
ALTER TABLE `reports_rpt_prt`
  ADD CONSTRAINT `reports_rpt_Prt_formato_id_8c46a6c2_fk_reports_F` FOREIGN KEY (`formato_id`) REFERENCES `reports_formatos` (`rep_frt_id`),
  ADD CONSTRAINT `reports_rpt_Prt_protocolo_id_84e57670_fk_protocols` FOREIGN KEY (`protocolo_id`) REFERENCES `protocols_protocolos` (`prt_id`);

--
-- Filtros para la tabla `reports_rpt_secc`
--
ALTER TABLE `reports_rpt_secc`
  ADD CONSTRAINT `reports_rpt_secc_formato_id_dd2e34a5_fk_reports_F` FOREIGN KEY (`formato_id`) REFERENCES `reports_formatos` (`rep_frt_id`),
  ADD CONSTRAINT `reports_rpt_secc_seccion_id_d48bd7e4_fk_protocols` FOREIGN KEY (`seccion_id`) REFERENCES `protocols_secciones` (`scc_id`);

--
-- Filtros para la tabla `reports_sistemas_tubos`
--
ALTER TABLE `reports_sistemas_tubos`
  ADD CONSTRAINT `reports_sistemas_tub_sistema_id_0cb88b7c_fk_machines_` FOREIGN KEY (`sistema_id`) REFERENCES `machines_sistemas` (`stm_id`),
  ADD CONSTRAINT `reports_sistemas_tubos_tubo_id_12e032cf_fk_machines_Tubos_tb_id` FOREIGN KEY (`tubo_id`) REFERENCES `machines_tubos` (`tb_id`);

--
-- Filtros para la tabla `tests_calculo_operacion`
--
ALTER TABLE `tests_calculo_operacion`
  ADD CONSTRAINT `tests_calculo_operac_calculo_id_4d540543_fk_tests_Pru` FOREIGN KEY (`calculo_id`) REFERENCES `tests_pruebacalculo` (`prb_cal_id`),
  ADD CONSTRAINT `tests_calculo_operac_operacion_id_763579b7_fk_operation` FOREIGN KEY (`operacion_id`) REFERENCES `operations_operaciones` (`opr_id`);

--
-- Filtros para la tabla `tests_prueba_tipos`
--
ALTER TABLE `tests_prueba_tipos`
  ADD CONSTRAINT `tests_prueba_tipos_calculo_id_97cc5014_fk_tests_Pru` FOREIGN KEY (`calculo_id`) REFERENCES `tests_pruebacalculo` (`prb_cal_id`),
  ADD CONSTRAINT `tests_prueba_tipos_opcion_id_19c87f70_fk_tests_Pru` FOREIGN KEY (`opcion_id`) REFERENCES `tests_pruebaopciones` (`prb_opc_id`),
  ADD CONSTRAINT `tests_prueba_tipos_seccion_id_a760d3c4_fk_protocols` FOREIGN KEY (`seccion_id`) REFERENCES `protocols_secciones` (`scc_id`);

--
-- Filtros para la tabla `token_blacklist_blacklistedtoken`
--
ALTER TABLE `token_blacklist_blacklistedtoken`
  ADD CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`);

--
-- Filtros para la tabla `token_blacklist_outstandingtoken`
--
ALTER TABLE `token_blacklist_outstandingtoken`
  ADD CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_User_user` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `user_historicaluser`
--
ALTER TABLE `user_historicaluser`
  ADD CONSTRAINT `User_historicaluser_history_user_id_99619363_fk_User_user_id` FOREIGN KEY (`history_user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD CONSTRAINT `User_user_groups_group_id_ca46cfeb_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `User_user_groups_user_id_8a581615_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD CONSTRAINT `User_user_user_permi_permission_id_6ee76041_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `User_user_user_permissions_user_id_321bdf68_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
