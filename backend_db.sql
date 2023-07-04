-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               11.0.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for tam
DROP DATABASE IF EXISTS `tam`;
CREATE DATABASE IF NOT EXISTS `tam` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `tam`;

-- Dumping structure for table tam.t_regularbaskets
CREATE TABLE IF NOT EXISTS `t_regularbaskets` (
  `BasketID` int(11) NOT NULL,
  `Description` varchar(255) DEFAULT '',
  `Donors` varchar(255) DEFAULT '',
  `WinningTicket` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`BasketID`),
  KEY `regularrelation` (`WinningTicket`),
  CONSTRAINT `regularrelation` FOREIGN KEY (`WinningTicket`) REFERENCES `t_regulartickets` (`TicketID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table tam.t_regularbaskets: ~0 rows (approximately)

-- Dumping structure for table tam.t_regulartickets
CREATE TABLE IF NOT EXISTS `t_regulartickets` (
  `TicketID` int(11) NOT NULL DEFAULT 0,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `PhoneNumber` varchar(50) DEFAULT NULL,
  `PrefersText` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`TicketID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table tam.t_regulartickets: ~1 rows (approximately)
INSERT INTO `t_regulartickets` (`TicketID`, `FirstName`, `LastName`, `PhoneNumber`, `PrefersText`) VALUES
	(0, 'No', 'Winner', 'Selected', 0);

-- Dumping structure for table tam.t_specialtybaskets
CREATE TABLE IF NOT EXISTS `t_specialtybaskets` (
  `BasketID` int(11) NOT NULL,
  `Description` varchar(255) DEFAULT '',
  `Donors` varchar(255) DEFAULT '',
  `WinningTicket` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`BasketID`) USING BTREE,
  KEY `specialtyrelation` (`WinningTicket`),
  CONSTRAINT `specialtyrelation` FOREIGN KEY (`WinningTicket`) REFERENCES `t_specialtytickets` (`TicketID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- Dumping data for table tam.t_specialtybaskets: ~0 rows (approximately)

-- Dumping structure for table tam.t_specialtytickets
CREATE TABLE IF NOT EXISTS `t_specialtytickets` (
  `TicketID` int(11) NOT NULL DEFAULT 0,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `PhoneNumber` varchar(50) DEFAULT NULL,
  `PrefersText` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`TicketID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- Dumping data for table tam.t_specialtytickets: ~1 rows (approximately)
INSERT INTO `t_specialtytickets` (`TicketID`, `FirstName`, `LastName`, `PhoneNumber`, `PrefersText`) VALUES
	(0, 'No', 'Winner', 'Selected', 0);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
