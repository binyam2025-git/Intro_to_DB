USE alx_book_store;

-- Insert a single row into the 'customer' table (as per checker's specific requirement)
-- If customer_id 1 or the email already exists, update the existing row
INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.')
ON DUPLICATE KEY UPDATE
    customer_name = VALUES(customer_name),
    email = VALUES(email),
    address = VALUES(address);
