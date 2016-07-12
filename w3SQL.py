#
# 1. Write a query to display the names (first_name, last_name) and
# salary for all employees whose salary is not
# in the range $10,000 through $15,000. 
#
SELECT first_name, last_name, salary
from employees
where salary < 10000 or salary > 15000; 

#
# 2. Write a query to display the names (first_name, last_name) and
# department ID of all employees in departments 30 or 100 in ascending
# alphabetical order by department ID.
#
SELECT first_name, last_name, department_ID 
From employees
where (department_ID = 30) or (department_ID = 100)
order by department_ID ASC;

#
# Write a query to display the names (first_name, last_name)
# and salary for all employees whose salary is not in the range
# $10,000 through $15,000 and are in department 30 or 100.
#
SELECT first_name, last_name, salary
FROM employees
where salary < 1000 or salary > 15000
and (emloyees.department_ID = 30) or (employees.department_ID = 100);

#
# Write a query to display the names (first_name, last_name)
# and hire date for all employees who were hired in 1987.
#
SELECT first_name, last_name, hire_date
FROM employees
where YEAR(hire_date) LIKE  '%87%'; 

#
# 5. Write a query to display the first_name of all employees
# who have both "b" and "c" in their first name.
#
SELECT first_name
FROM employees
where first_name LIKE '%b%' and first_name LIKE '%c%';

#
# 6. Write a query to display the last name, job, and salary
# for all employees whose job is that of a Programmer or a
# Shipping Clerk, and whose salary is not equal to $4,500,
# $10,000, or $15,000.
#
SELECT last_name, job, salary
FROM employees
where (job == 'Programmer') or (job == 'Shipping Clerk')
and (salary != 4500) and (salary != 10000) and (salary != 15000);

#
# 7. Write a query to display the last names of employees
# whose names have exactly 6 characters.
#
SELECT last_name
FROM employees
where last_name LIKE '______';

#
# 8. Write a query to display the last names of employees
# having 'e' as the third character. Go to the editor
#
SELECT last_name
FROM employees
where last_name LIKE '__e%';

#
# 9. Write a query to display the jobs/designations available
# in the employees table.
#
SELECT DISTINCT JOB_ID
From employees;

#
# 10. Write a query to display the names (first_name, last_name),
# salary and PF (15% of salary) of all employees.
#

SELECT first_name, last_name, salary, (salary/15) PF
from employees;

#
# 11. Write a query to select all record from employees
# where last name in 'BLAKE', 'SCOTT', 'KING' and 'FORD'. 
#
SELECT *
FROM employees
where last_name in ('BLAKE', 'SCOTT', 'KING', 'FORD'); 
