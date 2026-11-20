CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select distinct salary 
      from (
        select *, dense_rank() over (order by salary desc) as t
        from employee
      ) as f
      where t=n

  );
END