select distinct a.num as ConsecutiveNums
from Logs a inner join Logs b on (a.id = b.id - 1 and a.num = b.num)
    inner join Logs c on (a.id = c.id - 2 and a.num = c.num)
