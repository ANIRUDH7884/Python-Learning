create database practise ;
use practise;

#1. Table Creation 
create table employee_details(
Employee_id int primary key,
First_name varchar(50),
Last_name varchar(50),
Gender varchar(10),
Age int,
Department varchar(20),
Designation varchar(20),
Salary int,
City varchar(20),
Joining_Date date
);

#2. Insert 10 Records
INSERT INTO employee_details
(Employee_id, First_name, Last_name, Gender, Age, Department, Designation, Salary, City, Joining_Date)
VALUES
(1, 'Anirudh', 'T Anil', 'Male', 22, 'Software', 'Software Developer', 58000, 'Kochi', '2024-12-17'),
(2, 'Rahul', 'Menon', 'Male', 25, 'HR', 'HR Executive', 35000, 'Kochi', '2023-06-10'),
(3, 'Akhil', 'Nair', 'Male', 28, 'Finance', 'Accountant', 40000, 'Trivandrum', '2022-03-15'),
(4, 'Sneha', 'Pillai', 'Female', 24, 'Software', 'Frontend Developer', 50000, 'Kollam', '2024-01-20'),
(5, 'Meera', 'Krishnan', 'Female', 30, 'Marketing', 'Marketing Manager', 60000, 'Kochi', '2021-11-05'),
(6, 'Arjun', 'Varma', 'Male', 27, 'Software', 'Backend Developer', 55000, 'Calicut', '2023-08-12'),
(7, 'Divya', 'Suresh', 'Female', 26, 'HR', 'HR Manager', 45000, 'Trivandrum', '2022-07-18'),
(8, 'Vishnu', 'Das', 'Male', 29, 'Finance', ' Analyst', 52000, 'Kollam', '2021-09-25'),
(9, 'Anu', 'Joseph', 'Female', 23, 'Support', 'Customer Support', 30000, 'Kochi', '2024-04-02'),
(10, 'Kiran', 'Kumar', 'Male', 31, 'Software', 'Team Lead', 70000, 'Calicut', '2020-12-30');

#Basic Queries
#1. Display All Records
select * from employee_details ; 

#2 . Display first name department salary
select First_name , Department, Salary from employee_details;

#3. . Display employees whose salary is greater than ₹50,000. 
select * from employee_details where salary > 50000 ;

#4. Display employees whose salary is less than ₹40,000. 
select * from employee_details where salary < 40000;

#5. Display female employees. 
select * from employee_details where Gender = "Female" ;

#6. Display employees working in the IT department. 
select * from employee_details where Department = "software";

#7. Display employees whose age is greater than 30 years. 
select * from employee_details where Age > 30 ;

#8. Display employees whose first name starts with the letter 'A'. 
select * from employee_details where First_name like "A%";

#9. Display employees whose last name ends with the letter 'N'. 
select * from employee_details where First_name like "%N";

#10. Display employees ordered by salary in descending order.
select * from employee_details where salary order by salary desc ;

#Aggregate Functions 
#11. Find the total number of employees. 
select count(*) from employee_details as total_employees;

#12. Find the highest salary. 
select max(Salary) as Highest_salary from employee_details  ;

#13. Find the lowest salary. 
select min(Salary)  as Lowest_salary from employee_details ;

#14. Find the average salary. 
select avg(Salary) as Average_Salary from employee_details ;

#15. Find the total salary paid to all employees. 
select sum(Salary) as Total_Salary from employee_details ;

#GROUP BY & HAVING 
#16. Count the number of employees in each department. 
select Department , count(*) from employee_details group by Department ;

#17. Find the average salary of each department. 
select Department , avg(Salary) as Averge_Salary from employee_details group by Department;

#18. Find the maximum salary in each department. 
select Department , max(Salary) as Maximum_Salary from employee_details group by Department;

#19. Display departments having more than one employee. 
select Department , count(*) as Total_Employers from employee_details group by  Department having Total_Employers > 1 ;

#20. Display departments where the average salary is greater than ₹45,000. 
select  Department , avg(Salary) as Average_Salary from employee_details group by Department having Average_Salary > 45000 ;

#SQL Functions 
#21. Display employee names in uppercase. 
select upper(First_name) as Names from employee_details ;

#22. Display employee names in lowercase. 
select lower(Last_name) as Names from employee_details ;

#23. Find the length of each employee's first name. 
select length(First_name) from employee_details ;

#24. Display the current date. 
select curdate();

#25. Display the year of joining  for each employee.
select First_name ,  year(Joining_Date) as Joining_Year  from employee_details ;
