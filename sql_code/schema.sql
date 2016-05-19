-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema ice_cream_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ice_cream_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ice_cream_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `ice_cream_db` ;

-- -----------------------------------------------------
-- Table `ice_cream_db`.`ice_creams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ice_cream_db`.`ice_creams` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
