CREATE TABLE IF NOT EXISTS `suppliers` (
  `id` INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL
);