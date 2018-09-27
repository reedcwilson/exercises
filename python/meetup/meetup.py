import calendar
from datetime import date


def get_day(days, which):
    if which == "teenth":
        return next(filter(lambda d: d >= 13 and d <= 19, days))
    elif which == "last":
        return days[-1]
    else:
        return days[int(which[0]) - 1]


def meetup_day(year, month, day_of_week, which):
    day_num = list(calendar.day_name).index(day_of_week)
    weeks = calendar.Calendar().monthdayscalendar(year, month)
    days = [week[day_num] for week in weeks if week[day_num] != 0]
    return date(year, month, get_day(days, which))
