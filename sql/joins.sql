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


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_amount INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Acme Corp', 'New York'),
(2, 'TechStart Inc', 'San Francisco'),
(3, 'Global Logistics', 'Chicago'),
(4, 'Retail Solutions', 'Austin');

INSERT INTO orders VALUES
(1001, 1, 1500),
(1002, 2, 3400),
(1003, 1, 850),
(1004, 3, 5200),
(1005, 4, 1200);

SELECT 
    c.customer_id, c.customer_name, o.order_id, o.order_amount
FROM customers c
INNER JOIN orders o 
ON o.customer_id = c.customer_id;

-- LEFT JOIN --->

SELECT 
 e.emp_id , e.emp_name , d.department_name 
from employees e 
left join departments d 
on e.department_id = d.department_id;

select
 e.emp_id , e.emp_name , d.department_name 
from departments d 
left join employees e
on d.department_id = e.department_id;

-- Right Outer JOin / Right Join -- >
SELECT 
 e.emp_id , e.emp_name , d.department_name 
from employees e 
right join departments d 
on e.department_id = d.department_id;

select
 e.emp_id , e.emp_name , d.department_name 
from departments d 
right join employees e
on d.department_id = e.department_id;

-- Union Join -->
select
 e.emp_id , e.emp_name , d.department_name 
from employees e 
left join departments d 
on e.department_id = d.department_id
union
SELECT 
 e.emp_id , e.emp_name , d.department_name 
from employees e 
right join departments d 
on e.department_id = d.department_id;

-- SET OPERATIONS --

CREATE TABLE student_commerce (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    branch VARCHAR(50)
);

CREATE TABLE student_science (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    branch VARCHAR(50)
);

INSERT INTO student_commerce VALUES
(1, 'Arjun', 'Commerce'),
(2, 'Rahul', 'Commerce'),
(3, 'Sneha', 'Commerce'),
(4, 'Meera', 'Commerce'),
(5, 'Kiran', 'Commerce');

INSERT INTO student_science VALUES
(3, 'Sneha', 'Science'),
(4, 'Meera', 'Science'),
(5, 'Kiran', 'Science'),
(6, 'Anjali', 'Science'),
(7, 'Vikram', 'Science');
