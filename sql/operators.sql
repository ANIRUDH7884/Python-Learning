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

-- Like --
-- special Operators are % and _
select * from job_placement where college_name like "c%";
select * from job_placement where name like "j_______";
select * from job_placement where college_name like "%a";

-- distinct -- to find unique values

select distinct(stream) from job_placement;
select distinct(college_name) from job_placement;

-- Sql Functions --

-- Number Function
select abs(gpa) as grade_point from job_placement;

select round(1.8998,2) as result;

select ceiling(1.9872)as result;

select floor(3.902) as result ;

select power(2,3) as power;

select sqrt(100) as square;

select truncate(3.567,2);

select rand();

select 15 % 3 as remainder;

select sign(0) as sign;

-- String Function

select upper(name) , stream,college_name from job_placement;
select lower(name) , stream,college_name from job_placement;

select length("Anirudh T Anil") as length;
select trim("Anirudh T Anil") as result;

select concat("hello"," Anirudh") as result;

select replace('I like java','like','love') as reult;

select ltrim('  ANIRUDH') AS RESULT;
select rtrim('Anirudh   ')as Coki;
