--List the following details of each employee: employee number, last name, first name, gender, and salary
SELECT emp.emp_no as "employee number"
, emp.last_name as "last name"
, emp.first_name as "first name"
, emp.gender as "gender"
, sal.salary as "salary"

FROM employees as emp
JOIN salaries as sal
ON emp.emp_no = sal.emp_no;

--List employees who were hired in 1986.

SELECT emp.emp_no as "employee number"
, emp.last_name as "last name"
, emp.first_name as "first name" 
,emp.hire_date
from employees as emp
where emp.hire_date BETWEEN '1986-01-01' AND '1987-01-01';


--List the manager of each department with the following information:
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
select 
dm.dept_no as "department number"
,d.dept_name as "department name"
,dm.emp_no as "managers employee number" 
,emp.first_name as "first name"
,emp.last_name as "last name"
,dm.from_date as"start date"
,dm.to_date as "end date"
from departments as d 
JOIN dept_manager as dm
ON d.dept_no = dm.dept_no
JOIN employees as emp
ON dm.emp_no = emp.emp_no;

--List the department of each employee with the following information: 
--employee number, last name, first name, and department name.

SELECT de.emp_no as "employee number"
, emp.last_name as "employee last name"
, emp.first_name as "employee first name"
, d.dept_name as "employee department name"
FROM dept_emp as de
JOIN employees as emp
ON de.emp_no = emp.emp_no
JOIN departments as d
ON de.dept_no = d.dept_no;

--List all employees whose first name is "Hercules" and last names begin with "B."
select emp.first_name as "first name"
,emp.last_name as "last name"
from employees as emp
where emp.first_name = 'Hercules'
and emp.last_name LIKE 'B%';

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
select de.emp_no as "employee number"
, emp.last_name as "employee last name"
, emp.first_name as "employee first name"
, d.dept_name as "department name"

from dept_emp as de
join employees as emp
ON de.emp_no = emp.emp_no
JOIN departments as d
ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Sales';

--List all employees in the Sales and Development departments,
--including their employee number, last name, first name, and department name.
select de.emp_no as "employee number"
, emp.last_name as "employee last name"
, emp.first_name as "employee first name"
, d.dept_name as "department name"

from dept_emp as de
join employees as emp
ON de.emp_no = emp.emp_no
JOIN departments as d
ON de.dept_no = d.dept_no
where d.dept_name = 'Sales'
or d.dept_name= 'Development';


--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select
last_name
,count(last_name) as "frequency count ofemplpyees last name"
from employees
group by last_name
order by
count(last_name) DESC;