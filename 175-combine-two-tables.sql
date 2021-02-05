select FirstName, LastName, City, State
from Person as a left join Address as b on (a.PersonId = b.PersonId)
