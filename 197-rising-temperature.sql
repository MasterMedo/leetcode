select a.Id
from Weather a left join Weather b on (subdate(a.recordDate, 1) = b.recordDate)
where a.temperature > b.temperature
