from datetime import date
from calendar import day_name


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return day_name[date(day=day, month=month, year=year).weekday()]
