# Write your MySQL query statement below
select a.name
from employee a
join employee b on a.id=b.managerid
group by a.id
having count(a.id)>=5;