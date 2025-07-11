# Write your MySQL query statement below
select max(num) as num
from
(SELECT 
   num
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) = 1
order by num desc) as other;