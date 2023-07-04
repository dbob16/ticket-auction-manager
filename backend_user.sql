-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               11.0.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

CREATE USER 'tam'@'%' IDENTIFIED BY 'securepassword';
GRANT USAGE ON *.* TO 'tam'@'%';
GRANT EXECUTE, SELECT, SHOW VIEW, ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE VIEW, DELETE, DROP, EVENT, INDEX, INSERT, REFERENCES, TRIGGER, UPDATE, LOCK TABLES  ON `tam`.* TO 'tam'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;