with duplicate as (
    select b.Id
    from Person a, Person b
    where a.Email = b.Email and a.Id < b.Id
)

delete from Person
where Id in (
    select Id from duplicate
)
