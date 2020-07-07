-- -----------------------------------------------------
-- Schema mydb for MariaDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb4 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`dono_pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dono_pet` (
  `id_dono` INT AUTO_INCREMENT PRIMARY KEY,
  `nome_dono` VARCHAR(45) NOT NULL,
  `endereço_dono` VARCHAR(100) NOT NULL,
  `telefone_dono` VARCHAR(14) NOT NULL,
);


-- -----------------------------------------------------
-- Table `mydb`.`racao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`racao` (
  `id_racao` INT AUTO_INCREMENT PRIMARY KEY,
  `marca_racao` VARCHAR(45) NOT NULL,
  `quant_racao` DOUBLE(7,3) NOT NULL,
  `quant_diaria_racao` DOUBLE(7,3) NOT NULL,
  `data_compra_racao` DATE NULL,
);


-- -----------------------------------------------------
-- Table `mydb`.`tipo_pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tipo_pet` (
  `id_tipo_pet` INT AUTO_INCREMENT PRIMARY KEY,
  `categoria_tipo_pet` VARCHAR(50) NOT NULL,
);


-- -----------------------------------------------------
-- Table `mydb`.`pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet` (
  `id_pet` INT AUTO_INCREMENT PRIMARY KEY,
  `nome_pet` VARCHAR(45) NOT NULL,
  `id_tipo_pet` INT NOT NULL,
   FOREIGN KEY (`id_tipo_pet`) REFERENCES `mydb`.`tipo_pet` (`id_tipo_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table `mydb`.`vacinas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`vacinas` (
  `id_vacinas` INT AUTO_INCREMENT PRIMARY KEY,
  `nome_vacinas` VARCHAR(45) NOT NULL,
  `valor_vacinas` DOUBLE(7,2) NOT NULL,
  `observ_vacinas` TEXT NULL,
  `pet_id_pet` INT NOT NULL,
   FOREIGN KEY (`pet_id_pet`) REFERENCES `mydb`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table `mydb`.`alimentacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`alimentacao` (
  `id_alimentacao` INT NOT NULL AUTO_INCREMENT,
  `quantidade_alimentacao` DOUBLE(7,3) NOT NULL,
  `data_alimentacao` DATE NOT NULL,
  `horario_alimentacao` TIME NOT NULL,
  `pet_id_pet` INT NOT NULL,
   FOREIGN KEY (`pet_id_pet`) REFERENCES `mydb`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table `mydb`.`hist_peso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`hist_peso` (
  `id_hist_peso` INT AUTO_INCREMENT PRIMARY KEY,
  `peso` DOUBLE(7,3) NOT NULL,
  `data` DATE NOT NULL,
  `pet_id_pet` INT NOT NULL,
   FOREIGN KEY (`pet_id_pet`) REFERENCES `mydb`.`pet` (`id_pet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
); 


-- -----------------------------------------------------
-- Table `mydb`.`gastos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`gastos` (
  `id_gastos` INT AUTO_INCREMENT PRIMARY KEY,
  `preco_gastos` DOUBLE(7,2) NOT NULL,
  `loja_gastos` VARCHAR(30) NOT NULL,
  `desc_gastos` TEXT NULL,
  `data_gastos` DATE NULL,
  `id_dono` INT NOT NULL,
  FOREIGN KEY (`id_dono`) REFERENCES `mydb`.`dono_pet` (`id_dono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table `mydb`.`tipo_alerta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tipo_alerta` (
  `id_tipo_alerta` INT AUTO_INCREMENT PRIMARY KEY,
  `categoria_alerta` VARCHAR(50) NOT NULL,
);


-- -----------------------------------------------------
-- Table `mydb`.`alerta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`alerta` (
  `id_alerta` INT AUTO_INCREMENT PRIMARY KEY,
  `data_alerta` DATETIME NOT NULL,
  `id_dono` INT NOT NULL,
  `id_tipo_alerta` INT NOT NULL,
  `situacao` boolean NOT NULL,
  `descricao_alerta` TEXT,
   FOREIGN KEY (`id_dono`) REFERENCES `mydb`.`dono_pet` (`id_dono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`id_tipo_alerta`) REFERENCES `mydb`.`tipo_alerta` (`id_tipo_alerta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);
