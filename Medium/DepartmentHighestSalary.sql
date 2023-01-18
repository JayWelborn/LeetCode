# Write your MySQL query statement below
WITH highest_per_department AS (
    SELECT max(salary) as max_sal, departmentId
    FROM Employee
    GROUP BY departmentId
) SELECT
d.name as Department,
e.name as Employee,
e.salary as Salary
FROM Employee e
INNER JOIN highest_per_department ON e.salary = highest_per_department.max_sal AND e.departmentId = highest_per_department.departmentId
INNER JOIN Department d ON e.departmentId = d.id;
