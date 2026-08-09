create database employee;
use employee;

create table employee_details (
Emp_id int primary key,
Emp_name varchar(20),
Emp_age int,
Department varchar(30)
);

alter table employee_details
add column email varchar(150);

alter table employee_details
rename column email to Emp_email;

show tables;
describe employee_details;

create table products (
Product_id int auto_increment PRIMARY KEY,
product_name varchar(100) not null,
product_price decimal(10,2) not null check (product_price > 0),
product_stock int default 0,
unique(product_name)
);

alter table products
modify column product_name varchar(150);

