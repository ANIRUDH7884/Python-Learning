use job_placement;
select * from job_placement;

select * from job_placement where stream = "Computer Science";
select id,name,stream,college_name from job_placement where placement_status = "placed";

-- Arithemetic Operator -->
select name,salary,salary + 500 as Bonus from job_placement;
select name as emp_name,salary from job_placement; 

-- Relational Operator -->
select * from job_placement where salary >= 50000;
select * from job_placement where age = 25;
select * from job_placement where age != 25;

-- Logical Operator -->
select * from job_placement where gender = "Male" AND salary >= 60000;
select * from job_placement where college_name = "University of California--San Francisco" or age = 23;
select * from job_placement where gender != "Male";

-- Special Operator -->

-- In --
select * from job_placement where stream in ('Mechanical Engineering','Information Technology');
SELECT name,stream,gpa from job_placement where college_name in ('Stanford University',"Yale University");

-- Not In -- 
select * from job_placement where stream not in ('Mechanical Engineering','Information Technology');
SELECT name,stream,gpa from job_placement where college_name not in ('Stanford University',"Yale University");

-- Between --
select * from job_placement where salary between 50000 and 60000 ;
select * from job_placement where salary not between 50000 and 60000 ;

-- is Null --
select * from job_placement where stream is null;

-- is not null -- 
select * from job_placement where stream is not null;
