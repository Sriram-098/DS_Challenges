select employeeuni.unique_id as unique_id ,name from 
employees
left join employeeuni on  employees.id=employeeuni.id;