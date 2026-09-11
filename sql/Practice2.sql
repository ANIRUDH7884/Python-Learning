create Database Analysis ;
use Analysis ;

#Q1 . Display all employees. 
select * from employees ;

#Q2. Show employees from Egypt. 
select * from employees where Country = "Egypt";

#Q3. Show employees working in Manufacturing department. 
select * from employees where Department = "Manufacturing";

#Q4. Display employees whose Job Rate is 5. 
select * from employees where `Job Rate` = 5;

#Q5. Find employees with Monthly Salary greater than 3000. 
select * from employees where `Monthly Salary` > 3000;

#Q6. Find employees with Annual Salary less than 25000. 
select * from employees where `Annual Salary` < 25000;

#Q7. Employees having exactly 8 years of experience. 
select * from employees where Years = 8 ;

#Q8. Employees having more than 8 years experience. 
select * from employees where Years > 8 ;

#Q9. Employees whose overtime hours are not zero. 
select * from employees where `Overtime Hours` != 0;

#Q10. Employees with unpaid leaves greater than 2. 
select * from employees where `Unpaid Leaves` > 2;

#Q11. Employees from Egypt working in Sales. 
select * from employees where Country = "Egypt" and Department = "Sales" ;

#Q12. Employees earning more than 2500 and Job Rate 5. 
select * from employees where `Monthly Salary` > 2500 and `Job Rate` = 5;

#Q13. Employees with 8+ years experience and salary above 3000. 
select * from employees where Years > 8 and `Monthly Salary` > 3000;