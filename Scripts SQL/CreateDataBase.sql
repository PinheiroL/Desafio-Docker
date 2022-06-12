--criar base de dados crud_python_bd
DROP DATABASE IF EXISTS `crud_python_bd`;
CREATE DATABASE `crud_python_bd`;
USE `crud_python_bd`;

-- criar tabela cliente
CREATE TABLE `cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `cpf` varchar(12) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Inserindo dados para teste
INSERT INTO `cliente` (`id`, `nome`, `cpf`, `telefone`) VALUES
(1,	'Maria',	'21014739098',	'3499998888'),
(2,	'Joao',	'39175679035',	'9927347131');

COMMIT;