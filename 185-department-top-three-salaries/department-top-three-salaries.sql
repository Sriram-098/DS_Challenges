select department.name as Department ,t.name as Employee,t.salary as Salary
from 
(
    select *,
    dense_rank() over (partition by departmentID order by salary desc) as rn
    from employee
)as t

join department on t.departmentid=department.id
where rn<=3;