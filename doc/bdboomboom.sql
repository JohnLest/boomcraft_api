-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : mariadb:3306
-- Généré le : dim. 14 nov. 2021 à 18:18
-- Version du serveur : 10.6.5-MariaDB-1:10.6.5+maria~focal
-- Version de PHP : 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `bdboomboom`
--

-- --------------------------------------------------------

--
-- Structure de la table `FRIENDOF`
--

CREATE TABLE `FRIENDOF` (
  `idFrienof` int(11) NOT NULL,
  `idUsrAsc` int(11) NOT NULL,
  `idUserDes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `RESSOURCE`
--

CREATE TABLE `RESSOURCE` (
  `idRess` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `quantity` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `idType` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `TYPERESS`
--

CREATE TABLE `TYPERESS` (
  `idType` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `USER`
--

CREATE TABLE `USER` (
  `idUser` int(11) NOT NULL,
  `pseudo` varchar(12) NOT NULL,
  `mailAddress` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `FRIENDOF`
--
ALTER TABLE `FRIENDOF`
  ADD PRIMARY KEY (`idFrienof`),
  ADD KEY `idUsrAsc` (`idUsrAsc`),
  ADD KEY `idUserDes` (`idUserDes`);

--
-- Index pour la table `RESSOURCE`
--
ALTER TABLE `RESSOURCE`
  ADD PRIMARY KEY (`idRess`),
  ADD UNIQUE KEY `idName` (`name`),
  ADD KEY `idUser` (`idUser`) USING BTREE,
  ADD KEY `idType` (`idType`);

--
-- Index pour la table `TYPERESS`
--
ALTER TABLE `TYPERESS`
  ADD PRIMARY KEY (`idType`),
  ADD UNIQUE KEY `idNameType` (`name`);

--
-- Index pour la table `USER`
--
ALTER TABLE `USER`
  ADD PRIMARY KEY (`idUser`),
  ADD UNIQUE KEY `idmailAddress` (`mailAddress`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `FRIENDOF`
--
ALTER TABLE `FRIENDOF`
  ADD CONSTRAINT `FRIENDOF_ibfk_ASC` FOREIGN KEY (`idUsrAsc`) REFERENCES `USER` (`idUser`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FRIENDOF_ibfk_DES` FOREIGN KEY (`idUserDes`) REFERENCES `USER` (`idUser`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `RESSOURCE`
--
ALTER TABLE `RESSOURCE`
  ADD CONSTRAINT `Link_belongs` FOREIGN KEY (`idType`) REFERENCES `TYPERESS` (`idType`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Link_owns` FOREIGN KEY (`idUser`) REFERENCES `USER` (`idUser`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `USER`
--
ALTER TABLE `USER`
  ADD CONSTRAINT `USER_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `RESSOURCE` (`idUser`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
