select distinct a.id, a.visit_date, a.people
from Stadium a, Stadium b, Stadium c
where ((a.id = b.id - 1 and a.id = c.id - 2)
    or (a.id = b.id + 1 and a.id = c.id - 1)
    or (a.id = b.id + 2 and a.id = c.id + 1))
    and (a.people >= 100 and b.people >= 100 and c.people >= 100)
order by a.visit_date
