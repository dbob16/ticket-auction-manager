DROP DATABASE IF EXISTS tam;
CREATE DATABASE tam DEFAULT CHARACTER SET "utf8mb4";
USE tam;

CREATE TABLE regularticketst (
    ticketid INT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    phonenumber VARCHAR(50) DEFAULT "NA",
    preferstext SMALLINT DEFAULT 0
);
CREATE TABLE specialtyticketst (
    ticketid INT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    phonenumber VARCHAR(50) DEFAULT "NA",
    preferstext SMALLINT DEFAULT 0
);
INSERT INTO regularticketst (ticketid, firstname, lastname, phonenumber) VALUES (0, "Selected", "No Winner", "");
INSERT INTO specialtyticketst (ticketid, firstname, lastname, phonenumber) VALUES (0, "Selected", "No Winner", "");
CREATE TABLE regularbasketst (
    basketid INT PRIMARY KEY,
    description VARCHAR(255),
    donors VARCHAR(255),
    winningticket INT DEFAULT 0 REFERENCES regularticketst(ticketid)
);
CREATE TABLE specialtybasketst (
    basketid INT PRIMARY KEY,
    description VARCHAR(255),
    donors VARCHAR(255),
    winningticket INT DEFAULT 0 REFERENCES specialtyticketst(ticketid)
);
CREATE USER 'tam'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON tam.* TO 'tam'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;