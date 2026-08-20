-- Joins -->
create database new_schema;
use new_schema;

create table employees (
emp_id int primary key,
emp_name varchar(50),
department_id int
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments (department_id, department_name) 
VALUES
    (101, 'sales'),
    (102, 'Python'),
    (103, 'Data'),
    (104, 'AI');

INSERT INTO employees (emp_id, emp_name, department_id) 
VALUES
    (1, 'Alice Smith', 101),
    (2, 'Bob Jones', 102),
    (3, 'Charlie Brown', 103),
    (4, 'Diana Prince', 104),
    (5, 'Ethan Hunt', 101);
    
-- INNER JOIN -- 
select e.emp_id, e.emp_name , d.department_name from
employees e inner join departments d on e.department_id = d.department_id;

create table customers (
customer_id int primary key,
customer_name varchar(50),
city varchar(50)
);

create table orders(
order_id int primary key,
customer_id int,
order_amount int,
foreign key (customer_id) references customers(customer_id)
);

INSERT INTO customers (customer_id, customer_name, city) 
VALUES
    (1, 'Acme Corp', 'New York'),
    (2, 'TechStart Inc', 'San Francisco'),
    (3, 'Global Logistics', 'Chicago'),
    (4, 'Retail Solutions', 'Austin');

INSERT INTO orders (order_id, customer_id, order_amount) 
VALUES
    (1001, 1, 1500),
    (1002, 2, 3400),
    (1003, 1, 850),
    (1004, 3, 5200),
    (1005, 4, 1200);
    
SELECT 
    c.customer_id, c.customer_name, o.order_id, o.order_amount
FROM
    customers c
        INNER JOIN
    orders o ON o.customer_id = c.customer_id
ORDER BY o.order_amount DESC;