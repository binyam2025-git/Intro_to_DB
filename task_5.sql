-- Use the alx_book_store database
USE alx_book_store;

-- Insert a single row into the Customers table
-- If customer_id 1 or the email already exists, update the existing row
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.')
