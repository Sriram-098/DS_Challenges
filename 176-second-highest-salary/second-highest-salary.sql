# Write your MySQL query statement below

select max(salary) as secondhighestsalary
from employee
where salary<(
    select max(salary) from employee
);

/*select e.salary as  SecondHighestSalary
from (
    select *,dense_rank() over (order by salary desc) as rnk
    from employee
) as e
where rnk=2
limit 1;*/

