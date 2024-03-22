CREATE TABLE IF NOT EXISTS `orders` (
  `id` INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `buyer_id` INTEGER NOT NULL COMMENT "Codigo do comprador",
  `code` VARCHAR(40) NOT NULL COMMENT "Codigo do pedido",
  `creator_id` INTEGER NOT NULL COMMENT "Codigo do criador do pedido",
  `supplier_id` INTEGER NOT NULL COMMENT "Codigo do fornecedor",
  `quantity` NUMERIC(10,
  5) NOT NULL COMMENT "Quantidade do produto",
  `price` NUMERIC(10,
  2) NOT NULL COMMENT "Preço total da ordem",
  `product_id` INTEGER NOT NULL COMMENT "Codigo do produto",
  `product_price` NUMERIC(10,
  2) NOT NULL COMMENT "Preço do produto"
);
