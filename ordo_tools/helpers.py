from datetime import datetime
from datetime import timedelta

from ordo_tools.settings import YEAR

import dateutil.easter

import re


def findsunday(date: datetime) -> timedelta:
    """
    return the distance betweent the date and
    the previous Sunday, as timedelta.days
    """
    return timedelta(days=int(date.strftime('%w')))


def easter(year: int) -> datetime:
    """ return the date of easter for this year """
    return datetime(
        year=int(dateutil.easter.easter(year).strftime('%Y')),
        month=int(dateutil.easter.easter(year).strftime('%m')),
        day=int(dateutil.easter.easter(year).strftime('%d'))
    )


CHRISTMAS = datetime.strptime(str(YEAR) + "-12-25", "%Y-%m-%d")

FIRST_ADVENT = CHRISTMAS - findsunday(CHRISTMAS) - timedelta(weeks=3)

LAST_ADVENT = CHRISTMAS - timedelta(days=1)

EASTER_SEASON_START = easter(YEAR) - timedelta(weeks=6, days=4)

LENT_BEGINS = easter(YEAR) - timedelta(weeks=6, days=4)

LENT_ENDS = easter(YEAR) - timedelta(days=1)

EASTER = easter(YEAR)

EASTER_SEASON_END = easter(YEAR) + timedelta(days=39)

PENTECOST_SEASON_START = easter(YEAR) + timedelta(days=49)

PENTECOST_SEASON_END = FIRST_ADVENT - timedelta(days=1)


def day(year: int, month: int, day: int) -> datetime:
    return datetime(year=year, month=month, day=day)


def week(i: int) -> timedelta:
    """ return a timedelta week, with integers as the input """
    return timedelta(weeks=i)


def days(numdays: int) -> timedelta:
    """ return a timedelta day(s), with integers as the input """
    return timedelta(days=numdays)


def weekday(date: datetime) -> str:
    """ return the weekday, with datetime as the input """
    return date.strftime('%a')


def advance_a_day(date: str) -> str:
    """ return a date advanced a day, returns a string mm/dd """
    return date + timedelta(days=1)


def find_extra_epiphany(pents: int) -> int:
    """ return the number of Sundays not celebrated after Epiphany """
    if pents == 23:
        pass
    else:
        return pents - 24


# todo see if there is a more efficient way of taking care of this.
def leap_year(year: int) -> bool:
    """ return true if year is a leap year """
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def latex_replacement(string: str) -> str:
    """ return a string formatted for LaTeX with escape characters """
    return re.sub('&', r'\&', re.sub('_', r'\_', string))


def translate_month(month: str) -> str:
    """ return the latin name for a given english month """
    months_in_latin = {
        'January': 'Januarius',
        'February': 'Februarius',
        'March': 'Martius',
        'April': 'Aprilis',
        'May': 'Majus',
        'June': 'Junis',
        'July': 'Julius',
        'August': 'Augustus',
    }
    if month in months_in_latin:
        return months_in_latin[month]
    else:
        return month
