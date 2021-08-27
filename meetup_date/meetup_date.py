import datetime
from dataclasses import dataclass
from calendar import Calendar


@dataclass(frozen=True)
class Weekday:
    MONDAY: int = 0
    TUESDAY: int = 1
    WEDNESDAY: int = 2
    THURSDAY: int = 3
    FRIDAY: int = 4
    SATURDAY: int = 5
    SUNDAY: int = 6


class meetup_date:
    def __init__(self, year: int, month: int, nth: int = 4, weekday: int = Weekday.THURSDAY):
        self.cal: Calendar = Calendar()
        self.month: list = self.cal.monthdatescalendar(year, month)
        if nth > 0:
            self.meetup: datetime.date = list(
                filter(
                    lambda x: x.month == month and x.year == year,
                    map(
                        lambda x: x[weekday],
                        self.month
                    )
                )
            )[nth - 1]
        else:
            self.meetup: datetime.date = list(
                filter(
                    lambda x: x.month == month and x.year == year,
                    map(
                        lambda x: x[weekday],
                        self.month
                    )
                )
            )[nth]

    def __repr__(self):
        return repr(self.meetup)

    def __str__(self):
        return self.meetup.strftime('%Y-%m-%d')

    def __eq__(self, other):
        return self.meetup == other
