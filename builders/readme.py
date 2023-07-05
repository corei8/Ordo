from tools.feast import Feast

class Readme:
    def __init__(self, year: int, data: dict):
        self.year = year
        self.data = data

    @property
    def build(self):
        # mdldates = sorted(mdl)
        with open('README.md', 'a') as f:
            f.truncate(0)
            f.write(
                r"""
# Ordo

Traditional Catholic Ordo and Calendar.

## Python Specifications

Python 3.x.x 64-bit

### Dependencies:

[dateutil](https://dateutil.readthedocs.io/en/stable/)
```bash
pip install python-dateutil
```

## Overview

The temporal cycle is generated by a class as a dictionary. The sanctoral
cycle is made up of several files for country and diocese, and each file is
a "dynamic" dictionary contained in a class, which self-adjusts depending
on the year. The sanctoral cycle is the first to be compiled, then it is
added to the temporal cycle.

The output is a complex dictionary. Each key is a datetime object, and each
item contains the name of the feast together with all the data necessary to
determine the peculiarities of the office and Mass(es) of that day.

Easter is the first feast (every "event" is treated as a feast) to be
determined, since most of the liturgical year depends upon the date of
Easter. Christmas, being static with regard to its date, requires that we
only find the day of the week on which it falls. We begin building the
temporal calendar with January 1st.

## Progress

- [x] Temporal Calendar
- [x] Combined Temporal and Sanctoral Calendar
- [x] Method for adding other countries and dioceses
- [ ] Fasting rules
- [ ] Phases of the Moon
- [ ] Martyrology letter
- [ ] Commemorations
- [ ] Masses
- [ ] Vespers
- [x] Colors of Mass and Office
- [ ] Lessons for Laudes
- [ ] Our Lady's Saturday
- [ ] Prime
- [ ] Little Hours
- [ ] Solemnities
                        """)
            f.write('\n\n')
            f.write(f'## Sample Roman Calendar for {str(self.year)}')
            f.write('\n\n')
            f.write('| Day | Date | Feast |')
            f.write('\n')
            f.write('|---|---|---|')
            f.write('\n')
            for date in self.data:
                feast = Feast(date, self.data[date])
                f.write(
                    f'| {feast.translate_weekday} | {feast.readme_date} | {feast.name} |'
                )
                f.write('\n')
        return None
