with max_salaries as (
    select DepartmentId as Id, max(Salary) as Salary
    from Employee
    group by DepartmentId
)

select d.Name as Department, e.Name as Employee, e.Salary
from Employee e join Department d on (e.DepartmentId = d.Id)
    join max_salaries m on (e.DepartmentId = m.Id)
where e.Salary = m.Salary
