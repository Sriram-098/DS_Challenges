# Write your MySQL query statement below
select department.name as department,x.name as employee,x.salary
from (
    select *,dense_rank() over (partition by departmentid order by salary desc)as dnsk
    from employee
)as x
join department on x.departmentid=department.id
where dnsk<=3;
