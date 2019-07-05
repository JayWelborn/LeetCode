# Write your MySQL query statement below
SELECT ifnull(
    (SELECT DISTINCT salary AS SecondHighestSalary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1
    OFFSET 1), NULL)
AS SecondHighestSalary;
