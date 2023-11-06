-- CTE - my preference
WITH nums AS (
    SELECT
       id,
       num,
       LAG(num) OVER(ORDER BY id) as prev_num,
       LEAD(num) OVER(ORDER BY id) AS next_num
    FROM
       logs
)
SELECT DISTINCT
    num as ConsecutiveNums
FROM
    nums
WHERE num = prev_num AND num=next_num;

-- SubQuery
SELECT distinct num ConsecutiveNums
FROM (
  SELECT
    id,
    num,
    lag(num) over(order by id) as prev_num,
    lead(num) over(order by id) as next_num
  FROM logs
) next_prev
WHERE num=prev_num and prev_num=next_num;
