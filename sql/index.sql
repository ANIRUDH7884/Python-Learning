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

use employee;
alter table products rename to product_details;

drop table products;

#Insert
#creating values in products
insert into product_details (product_name,product_price,product_stock) values ('samsung a07','25000','8');

select * from product_details;

#alternative method
insert into employee_details values
(1,"Anirudh",22,'Software','anirudhtanil85@gmail.com'),
(2,"Komali",22,'Software','komali@gmail.com');

select * from employee_details;

truncate table employee_details;

create database sample;
drop database sample;

create table product_info(
pr_id int auto_increment primary key,
pr_name varchar(50),
man_place varchar(50),
expiry int
);

insert into product_info(pr_name,man_place,expiry) values
("samsung","Delhi", 70),
("OnePlus","Mumbai", 70),
("Apple","Goa", 70),
("Google","Kerala", 70);

select * from product_info;
select pr_name from product_info;

select * from product_info WHERE expiry = 70;
select pr_name from product_info where man_place = "Mumbai";

#Update
select * from product_info;
update product_info set man_place = "Raipur" where pr_id = 1;

#SAFE UPDATE MODE --> it prevents from accidentally delete or update too many rows from a table.

#to disable it 
set SQL_SAFE_UPDATES=0 ;

#DELETE

delete from product_info WHERE pr_id = 3;
select * from product_info;

#TCL -- Transaction Control Language
start transaction;
#begin;

select * from product_info;
insert into product_info values (5,"Vivo","Kerala",60);
savepoint x;
insert into product_info values (6,"Oppo","Kerala",60);
select * from product_info;

rollback;
commit;

delete from product_info where pr_id= 6;
