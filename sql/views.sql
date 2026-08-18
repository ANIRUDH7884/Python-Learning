create database college;
use college;

-- Create Main Student Table -- 
create table students (
s_id int primary key,
s_name varchar(50),
age int,
place varchar(50),
department varchar(50),
email varchar(100),
fees int
);

insert into students values
(1, 'Arjun', 20, 'Kochi', 'BCA', 'arjun@gmail.com', 25000),
(2, 'Meera', 21, 'Trivandrum', 'BCom', 'meera@gmail.com', 30000),
(3, 'Rahul', 22, 'Calicut', 'BSc', 'rahul@gmail.com', 28000),
(4, 'Anjali', 20, 'Kottayam', 'BCA', 'anjali@gmail.com', 26000),
(5, 'Vishnu', 23, 'Thrissur', 'BA', 'vishnu@gmail.com', 22000),
(6, 'Sneha', 21, 'Kannur', 'BBA', 'sneha@gmail.com', 27000);

select * from students;

create view ds_view as select * from students;

create view student_details as select * from students where department = "BCA";

SELECT * FROM student_details;


