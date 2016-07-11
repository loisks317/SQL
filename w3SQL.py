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
#
#
