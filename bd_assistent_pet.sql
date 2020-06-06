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
  `cpf_dono` VARCHAR(14) NOT NULL,
  `nome_dono` VARCHAR(45) NOT NULL,
  `endereço_dono` VARCHAR(100) NOT NULL,
  `telefone_dono` VARCHAR(14) NOT NULL,
  `email_dono` VARCHAR(45) NOT NULL,
  `senha_dono` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`cpf_dono`, `email_dono`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`racao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`racao` (
  `id_racao` INT NOT NULL,
  `marca_racao` VARCHAR(45) NOT NULL,
  `quant_racao` FLOAT(3,1) NOT NULL,
  `data_compra_racao` DATE NULL,
  `` VARCHAR(45) NULL,
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
  `porte` ENUM('pequeno', 'medio', 'grande') NOT NULL,
  `dono_pet_cpf_dono` VARCHAR(14) NOT NULL,
  `dono_pet_email_dono` VARCHAR(45) NOT NULL,
  `racao_id_racao` INT NOT NULL,
  PRIMARY KEY (`id_pet`),
  INDEX `fk_pet_dono_pet_idx` (`dono_pet_cpf_dono` ASC, `dono_pet_email_dono` ASC) VISIBLE,
  INDEX `fk_pet_racao1_idx` (`racao_id_racao` ASC) VISIBLE,
  CONSTRAINT `fk_pet_dono_pet`
    FOREIGN KEY (`dono_pet_cpf_dono` , `dono_pet_email_dono`)
    REFERENCES `mydb`.`dono_pet` (`cpf_dono` , `email_dono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pet_racao1`
    FOREIGN KEY (`racao_id_racao`)
    REFERENCES `mydb`.`racao` (`id_racao`)
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
  `dono_pet_cpf_dono` VARCHAR(14) NOT NULL,
  `dono_pet_email_dono` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_gastos`),
  INDEX `fk_gastos_dono_pet1_idx` (`dono_pet_cpf_dono` ASC, `dono_pet_email_dono` ASC) VISIBLE,
  CONSTRAINT `fk_gastos_dono_pet1`
    FOREIGN KEY (`dono_pet_cpf_dono` , `dono_pet_email_dono`)
    REFERENCES `mydb`.`dono_pet` (`cpf_dono` , `email_dono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`passeio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`passeio` (
  `id_passeio` INT NOT NULL AUTO_INCREMENT,
  `data_inicio_passeio` DATE NOT NULL,
  `horario_inicio_passeio` TIME NOT NULL,
  `data_inicio_passeio` DATE NOT NULL,
  `horario_inicio_passeio` TIME NOT NULL,
  `local_inicio_passeio` VARCHAR(45) NOT NULL,
  `local_parada_passeio` VARCHAR(45) NULL,
  `local_final_passeio` VARCHAR(45) NOT NULL,
  `pet_id_pet` INT NOT NULL,
  PRIMARY KEY (`id_passeio`),
  INDEX `fk_passeio_pet1_idx` (`pet_id_pet` ASC) VISIBLE,
  CONSTRAINT `fk_passeio_pet1`
    FOREIGN KEY (`pet_id_pet`)
    REFERENCES `mydb`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`alerta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`alerta` (
  `id_alerta` INT NOT NULL AUTO_INCREMENT,
  `tipo_alerta` ENUM('vacinacao', 'alimentacao') NOT NULL,
  `nome_alerta` VARCHAR(45) NOT NULL,
  `desc_alerta` VARCHAR(45) NOT NULL,
  `data_alerta` DATE NOT NULL,
  `horario_alerta` TIME NULL,
  `dono_pet_cpf_dono` VARCHAR(14) NOT NULL,
  `dono_pet_email_dono` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_alerta`),
  INDEX `fk_alerta_dono_pet1_idx` (`dono_pet_cpf_dono` ASC, `dono_pet_email_dono` ASC) VISIBLE,
  CONSTRAINT `fk_alerta_dono_pet1`
    FOREIGN KEY (`dono_pet_cpf_dono` , `dono_pet_email_dono`)
    REFERENCES `mydb`.`dono_pet` (`cpf_dono` , `email_dono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;