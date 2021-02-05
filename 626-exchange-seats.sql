select case when b.id is null then a.id else b.id end as id, a.student
from seat a left join seat b on (
    case
        when a.id & 1 then a.id = b.id - 1
        else a.id = b.id + 1
    end
)
order by id
