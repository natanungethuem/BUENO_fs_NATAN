
--Password decoded is 123456
INSERT INTO users (username, password) VALUES 
('admin', '$2b$12$PhLq3s33IodnZ2Vb1o1YnubweFn9zveWidK9ZXpR.bz.3dEEt1S0K'),
('requester01', '$2b$12$PhLq3s33IodnZ2Vb1o1YnubweFn9zveWidK9ZXpR.bz.3dEEt1S0K'),
('requester02', '$2b$12$PhLq3s33IodnZ2Vb1o1YnubweFn9zveWidK9ZXpR.bz.3dEEt1S0K'),
('buyer01', '$2b$12$PhLq3s33IodnZ2Vb1o1YnubweFn9zveWidK9ZXpR.bz.3dEEt1S0K'),
('buyer02', '$2b$12$PhLq3s33IodnZ2Vb1o1YnubweFn9zveWidK9ZXpR.bz.3dEEt1S0K')/


INSERT INTO `suppliers` (`name`, `address`, `email`) VALUES 
('Supplier 01', 'Supplier Address', 'supplier01@example.com'),
('Supplier 02', 'Supplier Address', 'supplier02@example.com');

INSERT INTO `products` (`name`, `price`) VALUES 
('Product 01', 90), 
('Product 02', 80);
