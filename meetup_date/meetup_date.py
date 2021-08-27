import enum
import datetime
from calendar import Calendar


class Weekday(enum.Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class meetup_date:
    def __init__(self, year: int, month: int, nth: int = 4, weekday: Weekday = Weekday.THURSDAY):
        if isinstance(weekday, int):
            weekday = Weekday(weekday)

        self.cal: Calendar = Calendar()
        self.month: list = self.cal.monthdatescalendar(year, month)
        if nth > 0:
            self.meetup: datetime.date = list(filter(lambda x: x >= datetime.date(year, month, 1), map(lambda x: x[nth - 1], self.month)))[weekday.value]
        else:
            self.meetup: datetime.date = list(filter(lambda x: x >= datetime.date(year, month, 1), map(lambda x: x[nth], self.month)))[weekday.value]

    def __repr__(self):
        return repr(self.meetup)

    def __str__(self):
        return self.meetup.strftime('%Y-%m-%d')
