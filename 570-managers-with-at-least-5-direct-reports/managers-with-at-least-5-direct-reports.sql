

select e1.name as name from employee e1
left join  employee e2 on e1.id=e2.managerid
group by e1.id
having count(*)>=5;