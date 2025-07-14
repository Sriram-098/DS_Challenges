select person_name  from (
select person_name,sum(weight) over (order by turn )as totalweight
from queue) as sub
where totalweight<=1000
ORDER BY totalweight desc
limit 1;