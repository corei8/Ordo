#####################################################
#                                                   #
#   (c) 2021 - GREGORY ROBERT BARNES                #
#   THIS SOFTWARE MAY NOT BE USED EXCEPT WITH THE   #
#   EXPLICIT PERMISSION OF GREGORY ROBERT BARNES.   #
#   corei8.github@gmail.com                         #
#                                                   #
#####################################################


def main(year: int, diocese: str):

    def set_global_year(year: int) -> None:
        """ Writes the global year to a file """
        with open("ordo_tools/settings.py", "w") as f:
            f.write('YEAR = ' + str(year))
        return None

    set_global_year(year)

    from ordo_tools.temporal_cycle import build_temporal
    from ordo_tools.utils import explode_octaves, stitch, dict_clean
    from ordo_tools.outputs import build_latex_ordo, readme_calendar, build_latin_calendar

    build_temporal(year)

    stitch(sanctoral=explode_octaves(region_diocese=diocese))
    dict_clean('calendar', '.')
    dict_clean('calendar', '_')
    # commemoration_ordering('calendar')
    build_latex_ordo(year)
    readme_calendar(year)
    
    # build_latin_calendar(year)


if __name__ == '__main__':
    main(year=2022, diocese='roman')
