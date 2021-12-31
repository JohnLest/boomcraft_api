-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Dec 31, 2021 at 11:07 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `boomcraft_api`
--

-- --------------------------------------------------------

--
-- Table structure for table `friend_of`
--

DROP TABLE IF EXISTS `friend_of`;
CREATE TABLE IF NOT EXISTS `friend_of` (
  `id_friend_of` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_user_asc` bigint(20) UNSIGNED NOT NULL,
  `id_user_des` bigint(20) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_friend_of`),
  KEY `id_user_asc` (`id_user_asc`),
  KEY `id_user_des` (`id_user_des`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `name_resource`
--

DROP TABLE IF EXISTS `name_resource`;
CREATE TABLE IF NOT EXISTS `name_resource` (
  `id_name_res` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_name_res`),
  UNIQUE KEY `id_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `name_resource`
--

INSERT INTO `name_resource` (`id_name_res`, `name`) VALUES
(7, 'archer'),
(4, 'food'),
(5, 'gold'),
(2, 'iron'),
(3, 'stone'),
(8, 'warrior'),
(1, 'wood'),
(6, 'worker');

-- --------------------------------------------------------

--
-- Table structure for table `resource`
--

DROP TABLE IF EXISTS `resource`;
CREATE TABLE IF NOT EXISTS `resource` (
  `id_res` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_type_res` int(11) UNSIGNED NOT NULL,
  `id_name_res` int(11) UNSIGNED NOT NULL,
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `quantity` int(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`id_res`),
  KEY `id_user` (`id_user`) USING BTREE,
  KEY `id_type_res` (`id_type_res`),
  KEY `id_name_res` (`id_name_res`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `type_resource`
--

DROP TABLE IF EXISTS `type_resource`;
CREATE TABLE IF NOT EXISTS `type_resource` (
  `id_type_res` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  PRIMARY KEY (`id_type_res`),
  UNIQUE KEY `id_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `type_resource`
--

INSERT INTO `type_resource` (`id_type_res`, `name`) VALUES
(2, 'material'),
(1, 'unit');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id_user` bigint(20) UNSIGNED NOT NULL,
  `pseudo` varchar(12) NOT NULL,
  `mail_address` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `id_pseudo` (`pseudo`),
  UNIQUE KEY `id_mail_address` (`mail_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `user`
--
DROP TRIGGER IF EXISTS `after_insert_user`;
DELIMITER $$
CREATE TRIGGER `after_insert_user` AFTER INSERT ON `user` FOR EACH ROW begin
	insert into
	    resource(id_type_res, id_name_res, id_user, quantity)
	values
	    (1, 8, new.id_user, 0),
	    (1, 7, new.id_user, 0),
	    (1, 6, new.id_user, 0),
	    (2, 5, new.id_user, 0),
	    (2, 4, new.id_user, 0),
	    (2, 3, new.id_user, 0),
	    (2, 2, new.id_user, 0),
	    (2, 1, new.id_user, 0);
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_resource`
-- (See below for the actual view)
--
DROP VIEW IF EXISTS `v_resource`;
CREATE TABLE IF NOT EXISTS `v_resource` (
`id_res` int(11) unsigned
,`id_user` bigint(20) unsigned
,`type` varchar(15)
,`resource` varchar(15)
,`quantity` int(11) unsigned
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_weight_resource`
-- (See below for the actual view)
--
DROP VIEW IF EXISTS `v_weight_resource`;
CREATE TABLE IF NOT EXISTS `v_weight_resource` (
`id_weight_res` int(11) unsigned
,`id_name_res` int(11) unsigned
,`name` varchar(15)
,`weight` int(11)
);

-- --------------------------------------------------------

--
-- Table structure for table `weight_resource`
--

DROP TABLE IF EXISTS `weight_resource`;
CREATE TABLE IF NOT EXISTS `weight_resource` (
  `id_weight_res` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_name_res` int(11) UNSIGNED NOT NULL,
  `weight` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_weight_res`),
  UNIQUE KEY `id_name_res` (`id_name_res`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `weight_resource`
--

INSERT INTO `weight_resource` (`id_weight_res`, `id_name_res`, `weight`) VALUES
(1, 1, 1),
(2, 3, 1),
(3, 4, 25),
(4, 2, 200),
(5, 5, 5846);

-- --------------------------------------------------------

--
-- Structure for view `v_resource`
--
DROP TABLE IF EXISTS `v_resource`;

DROP VIEW IF EXISTS `v_resource`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER VIEW `v_resource`  AS  select `r`.`id_res` AS `id_res`,`r`.`id_user` AS `id_user`,`tr`.`name` AS `type`,`nr`.`name` AS `resource`,`r`.`quantity` AS `quantity` from ((`resource` `r` join `type_resource` `tr` on(`r`.`id_type_res` = `tr`.`id_type_res`)) join `name_resource` `nr` on(`r`.`id_name_res` = `nr`.`id_name_res`)) ;

-- --------------------------------------------------------

--
-- Structure for view `v_weight_resource`
--
DROP TABLE IF EXISTS `v_weight_resource`;

DROP VIEW IF EXISTS `v_weight_resource`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER VIEW `v_weight_resource`  AS  select `wr`.`id_weight_res` AS `id_weight_res`,`wr`.`id_name_res` AS `id_name_res`,`nr`.`name` AS `name`,`wr`.`weight` AS `weight` from (`weight_resource` `wr` join `name_resource` `nr` on(`nr`.`id_name_res` = `wr`.`id_name_res`)) ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `friend_of`
--
ALTER TABLE `friend_of`
  ADD CONSTRAINT `friend_of_ibfk_1` FOREIGN KEY (`id_user_asc`) REFERENCES `user` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `friend_of_ibfk_2` FOREIGN KEY (`id_user_des`) REFERENCES `user` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `resource`
--
ALTER TABLE `resource`
  ADD CONSTRAINT `resource_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `resource_ibfk_2` FOREIGN KEY (`id_name_res`) REFERENCES `name_resource` (`id_name_res`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `resource_ibfk_3` FOREIGN KEY (`id_type_res`) REFERENCES `type_resource` (`id_type_res`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `weight_resource`
--
ALTER TABLE `weight_resource`
  ADD CONSTRAINT `weight_resource_ibfk_1` FOREIGN KEY (`id_name_res`) REFERENCES `name_resource` (`id_name_res`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
