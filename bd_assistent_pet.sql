SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`dono_pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dono_pet` (
  `id_dono` INT NOT NULL AUTO_INCREMENT,
  `nome_dono` VARCHAR(45) NOT NULL,
  `endereço_dono` VARCHAR(100) NOT NULL,
  `telefone_dono` VARCHAR(14) NOT NULL,
  PRIMARY KEY (`id_dono`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`racao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`racao` (
  `id_racao` INT NOT NULL,
  `marca_racao` VARCHAR(45) NOT NULL,
  `quant_racao` FLOAT(3,1) NOT NULL,
  `quant_diaria_racao` FLOAT(3,1) NOT NULL,
  `data_compra_racao` DATE NULL,
  PRIMARY KEY (`id_racao`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet` (
  `id_pet` INT NOT NULL AUTO_INCREMENT,
  `nome_pet` VARCHAR(45) NOT NULL,
  `data_nasc` DATE NOT NULL,
  `raça` VARCHAR(45) NOT NULL,
  `id_dono` INT NOT NULL AUTO_INCREMENT,
  `racao_id_racao` INT NOT NULL,
  PRIMARY KEY (`id_pet`),
  INDEX `fk_pet_dono_pet_idx` ('id_dono') VISIBLE,
  INDEX `fk_pet_racao1_idx` (`racao_id_racao` ASC) VISIBLE,
  CONSTRAINT `fk_pet_dono_pet`
    FOREIGN KEY ('id_dono')
    REFERENCES `mydb`.`dono_pet` ('id_dono')
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pet_racao1`
    FOREIGN KEY (`racao_id_racao`)
    REFERENCES `mydb`.`racao` (`id_racao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tipo_pet` (
  `id_tipo_pet` INT NOT NULL AUTO_INCREMENT,
  `categoria_tipo_pet` VARCHAR(50) NOT NULL,
  'id_pet' INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_tipo_pet`),
  INDEX `fk_tipo_pet_id_pet_idx` ('id_pet') VISIBLE,
  CONSTRAINT `fk_tipo_pet_id_pet`
    FOREIGN KEY ('id_pet')
    REFERENCES `mydb`.`pet` ('id_pet')
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`vacinas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`vacinas` (
  `id_vacinas` INT NOT NULL AUTO_INCREMENT,
  `nome_vacinas` VARCHAR(45) NOT NULL,
  `valor_vacinas` FLOAT(7,2) NOT NULL,
  `observ_vacinas` TEXT NULL,
  `pet_id_pet` INT NOT NULL,
  PRIMARY KEY (`id_vacinas`),
  INDEX `fk_vacinas_pet1_idx` (`pet_id_pet` ASC) VISIBLE,
  CONSTRAINT `fk_vacinas_pet1`
    FOREIGN KEY (`pet_id_pet`)
    REFERENCES `mydb`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`alimentacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`alimentacao` (
  `id_alimentacao` INT NOT NULL AUTO_INCREMENT,
  `quantidade_alimentacao` FLOAT(4,1) NOT NULL,
  `data_alimentacao` DATE NOT NULL,
  `horario_alimentacao` TIME NOT NULL,
  `` VARCHAR(45) NULL,
  `pet_id_pet` INT NOT NULL,
  PRIMARY KEY (`id_alimentacao`),
  INDEX `fk_alimentacao_pet1_idx` (`pet_id_pet` ASC) VISIBLE,
  CONSTRAINT `fk_alimentacao_pet1`
    FOREIGN KEY (`pet_id_pet`)
    REFERENCES `mydb`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`hist_peso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`hist_peso` (
  `id_hist_peso` INT NOT NULL AUTO_INCREMENT,
  `peso` FLOAT(6,3) NOT NULL,
  `data` DATE NOT NULL,
  `` VARCHAR(45) NULL,
  `pet_id_pet` INT NOT NULL,
  PRIMARY KEY (`id_hist_peso`),
  INDEX `fk_hist_peso_pet1_idx` (`pet_id_pet` ASC) VISIBLE,
  CONSTRAINT `fk_hist_peso_pet1`
    FOREIGN KEY (`pet_id_pet`)
    REFERENCES `mydb`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`gastos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`gastos` (
  `id_gastos` INT NOT NULL,
  `preco_gastos` FLOAT(6,2) NOT NULL,
  `loja_gastos` VARCHAR(30) NOT NULL,
  `desc_gastos` TEXT NULL,
  `data_gastos` DATE NULL,
  `` VARCHAR(45) NULL,
  `id_dono` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_gastos`),
  INDEX `id_dono` ('id_dono') VISIBLE,
  CONSTRAINT `fk_gastos_dono_pet1`
    FOREIGN KEY ('id_dono')
    REFERENCES `mydb`.`dono_pet` (`id_dono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`alerta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`alerta` (
  `id_alerta` INT NOT NULL AUTO_INCREMENT,
  `nome_alerta` VARCHAR(45) NOT NULL,
  `desc_alerta` VARCHAR(45) NOT NULL,
  `data_alerta` DATE NOT NULL,
  `horario_alerta` TIME NULL,
  `id_dono` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_alerta`),
  INDEX `fk_alerta_dono_pet1_idx` ('id_dono') VISIBLE,
  CONSTRAINT `fk_alerta_dono_pet1`
    FOREIGN KEY (`id_dono`)
    REFERENCES `mydb`.`dono_pet` (`id_dono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`tipo_alerta`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`tipo_alerta` (
  `id_tipo_alerta` INT NOT NULL AUTO_INCREMENT,
  'categoria_alerta' VARCHAR(50) NOT NULL,
  `id_alerta` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_tipo_alerta`),
  INDEX `fk_alerta_id_alerta_idx` ('id_alerta') VISIBLE,
  CONSTRAINT `fk_alerta_id_alerta`
    FOREIGN KEY (`id_alerta`)
    REFERENCES `mydb`.`alerta` (`id_alerta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;