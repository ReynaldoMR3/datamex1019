USE cars;
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cars
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cars
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cars` DEFAULT CHARACTER SET utf8mb4 ;
USE `cars` ;

-- -----------------------------------------------------
-- Table `cars`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`Cars` (
  `VIN` VARCHAR(25) NOT NULL COMMENT '			',
  `Manufacturer` TEXT NOT NULL,
  `Model` TEXT NOT NULL,
  `Year` INT(11) NOT NULL,
  `Color` TEXT NOT NULL,
  PRIMARY KEY (`VIN`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `cars`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`Customers` (
  `Customer ID` INT(11) NOT NULL,
  `Name` TINYTEXT NOT NULL,
  `Phone` VARCHAR(16) NOT NULL,
  `Email` VARCHAR(16) NULL DEFAULT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `City` TINYTEXT NOT NULL,
  `State/Province` TINYTEXT NOT NULL,
  `Country` TINYTEXT NOT NULL,
  `Postal` INT(11) NOT NULL,
  PRIMARY KEY (`Customer ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `cars`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`Invoices` (
  `Invoice Number` INT(11) NOT NULL,
  `Date` DATE NOT NULL,
  `Car` INT(11) NOT NULL,
  `Sales Person` INT(11) NOT NULL,
  PRIMARY KEY (`Invoice Number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `cars`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cars`.`Salespersons` (
  `Staff ID` INT(11) NOT NULL,
  `Name` MEDIUMTEXT NOT NULL,
  `Store` TINYTEXT NOT NULL,
  PRIMARY KEY (`Staff ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
