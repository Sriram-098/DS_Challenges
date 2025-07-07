# Write your MySQL query statement below
select register.contest_id ,round((count(distinct users.user_id)*100.0/(select count(distinct users.user_id) from users)),2) as percentage
from users
 join register on users.user_id=register.user_id
group by register.contest_id
order by percentage desc,
register.contest_id asc;
