CREATE DATABASE IF NOT EXISTS acme_store;
USE acme_store;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT NOT NULL
);

INSERT INTO books (title, author, year) VALUES
('The Art of Security', 'Alice Smith', 2020),
('Python for Professionals', 'Bob Jones', 2019),
('Modern Web Apps', 'Carol White', 2021),
('Legacy Systems', 'Dan Brown', 2018),
('Database Essentials', 'Eve Black', 2022); 