from importlib import import_module

from ordo_tools.feast import Feast

from ordo_tools.helpers import FIRST_ADVENT
from ordo_tools.helpers import LAST_ADVENT
from ordo_tools.helpers import LENT_BEGINS
from ordo_tools.helpers import LENT_ENDS
from ordo_tools.helpers import days
from ordo_tools.helpers import ladys_office
from ordo_tools.helpers import leap_year

from ordo_tools.liturgical_dates import integer_to_roman

from ordo_tools.temporal import Temporal

from sanctoral.diocese.roman import Sanctoral


class LiturgicalCalendar:

    def __init__(self, year, diocese, country=""):
        self.year = year
        self.diocese = diocese
        self.transfers = None
        self.temporal = Temporal(self.year).return_temporal()

    def explode_octaves(self, feast: Feast) -> dict:
        """
        Generates "explodes" the octave for a feast.
        """
        octave = {}
        for x in range(7):
            intro = f"De {integer_to_roman(x+2)} die"
            if x != 6:
                feast.name = f"{intro} infra {feast.infra_octave_name}"
            else:
                feast.name = feast.infra_octave_name
            feast.rank_v = "feria"
            feast.rank_n = 18 if x < 6 else 13  # common octave
            octave |= {feast.date+days(x+1): feast.updated_properties}
        return octave

    def find_octave(self, year: dict) -> dict:
        """
        Finds the octaves of the sanctoral cycle and adds
        them to the year.
        """
        y = year.copy()
        temporals = []
        for feast in self.temporal.values():
            temporals.append(feast["feast"])
        for date, feast in y.items():
            candidate = Feast(feast_date=date, properties=feast)
            if candidate.name in temporals:
                continue
            elif candidate.octave is True:
                octave = self.explode_octaves(candidate)
                y |= self.add_feasts(master=y, addition=octave)
        return y

    def commemoration(self, feast: Feast, com: Feast) -> Feast:
        """
        Adds one feast as the commemoration of another feast.
        """
        feast.com.insert(0, com.feast_properties)
        return feast

    def rank_by_nobility(self, feast_1: Feast, feast_2: Feast) -> dict:
        """
        Takes two feasts and returns the one with the higher rank.
        """
        alpha, bravo = feast_1.nobility, feast_2.nobility
        for x in range(6):
            if alpha[x] < bravo[x]:
                return {'higher': feast_1, 'lower': feast_2}
            elif alpha[x] > bravo[x]:
                return {'higher': feast_2, 'lower': feast_1}
            else:
                pass
        return {'higher': feast_1, 'lower': feast_2}

    def rank(self, dynamic: Feast, static: Feast) -> Feast:
        # TODO: this should return a Feast object.
        """
        Ranks feasts that occur on the same date. Send feasts that can be
        transferred to the transfer dictionary. "Dynamic" is from the
        sanctoral cycle, and "static" is from the temporal cycle.
        """
        # if the feasts are the same rank:
        if dynamic.rank_n == static.rank_n:
            return self.rank_by_nobility(
                    dynamic,
                    static
                )['higher'],
        else:
            candidates = {
                dynamic.rank_n: dynamic,
                static.rank_n: static,
            }
            higher = candidates[sorted(candidates)[0]]
            lower = candidates[sorted(candidates)[1]]
            if lower.rank_n == 22:
                pass
            if lower.rank_n == 19:  # lent
                return self.commemoration(
                        feast=higher,
                        com=lower
                    )

            # feasts that do not take a commemoration
            if higher.rank_n <= 4:
                # lower feast is transferred
                if lower.rank_n <= 10:
                    if lower.fasting is True:
                        higher.fasting = True
                    if lower != self.transfers:
                        self.transfers = lower
                    return higher
                else:
                    # lower feast is ignored
                    if lower.fasting is True:
                        higher.fasting = True
                    return higher
                # HACK: allows transfers to occur on ferias, etc.

            # impeded DM, D and SD
            elif 14 <= lower.rank_n <= 16:
                return self.commemoration(
                        feast=higher,
                        com=lower
                    )
            else:
                return self.commemoration(
                        feast=higher,
                        com=lower
                    )
        # return ranked_feasts

    def transfer_feast(self, feast: Feast) -> None:
        """
        Checks for feasts in the transfer dictionary.
        """
        return self.rank(dynamic=self.transfers, static=feast)

    def add_feasts(self, master: dict, addition: dict) -> dict:
        """
        Adds additional feasts to the master feast dictionary;
        Sends the feasts that confilict to the ranking function.
        """
        calendar = master.copy()
        for date, data in calendar.items():

            if date in addition:
                feast = self.rank(
                    dynamic=Feast(date, addition[date]),
                    static=Feast(date, data)
                )
            else:
                feast = Feast(date, data)

            if self.transfers is not None:
                print("transferring")
                result = self.transfer_feast(
                    Feast(date, feast.updated_properties)
                )
                print(result.feast)
                if result.feast == feast.feast:
                    print("no result")
                    pass
                else:
                    # WARN: this assumes that there is no transfer overlap
                    self.transfers = None
                    feast = result

            # TODO: rank the overlapping transfers
            try:
                calendar |= {date: feast.updated_properties}
            except TypeError:
                pass
        return calendar

    def our_ladys_saturday(self, calendar: dict) -> None:
        """
        Adds all the Saturday Offices of the Blessed Virgin
        to the temporal calendar.
        """
        # TODO: add mass number according to season
        year = calendar.copy()
        office = ladys_office
        for feast in year.keys():
            if feast.strftime("%w") == str(6):
                if LENT_BEGINS.date() <= feast.date() <= LENT_ENDS.date():
                    continue
                elif FIRST_ADVENT.date() <= feast.date() <= LAST_ADVENT.date():
                    continue
                else:
                    if year[feast]["rank"][0] > 16:  # not a double
                        year[feast] = office  # TODO: add commemorations
                    else:
                        continue
        return year

    def build(self) -> None:
        """ Stitches the temporal and sanctoral calendars together. """
        saints = Sanctoral(self.year)
        if self.diocese == 'roman':
            sanctoral = saints.data \
                if leap_year(self.year) is False else saints.leapyear()
        else:
            diocese = import_module(
                f"sanctoral.diocese.{self.diocese}",
            )
            sanctoral = diocese.Diocese(self.year).calendar()
        full_calendar = self.add_feasts(self.temporal, sanctoral).copy()
        full_calendar |= self.our_ladys_saturday(full_calendar)
        full_calendar |= self.find_octave(year=full_calendar)
        return full_calendar
