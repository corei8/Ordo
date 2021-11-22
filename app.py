#####################################################
#                                                   #
#   (c) 2021 - GREGORY ROBERT BARNES                #
#   THIS SOFTWARE MAY NOT BE USED EXCEPT WITH THE   #
#   EXPLICIT PERMISSION OF GREGORY ROBERT BARNES.   #
#   corei8.github@gmail.com                         #
#                                                   #
#####################################################


from ordo_tools.temporal_cycle import build_temporal
from ordo_tools.ordo_tools import *
from ordo_tools.outputs import build_latex_ordo


def app(year: int, diocese: str):
    global_year(year)
    build_temporal(year)
    explode_octaves(region_diocese='roman')
    dict_clean('roman', '_')
    stitch(diocese)
    dict_clean('calendar', '.')
    # readme_calendar(year)
    build_latex_ordo(year)

 # todo use os to get a list of the dioceses or regions needed to complete an ordo


# 2024 is a leap year
app(year=2022, diocese="roman")
