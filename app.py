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
    stitch(sanctoral=explode_octaves(region_diocese=diocese))
    dict_clean('calendar', '.')
    dict_clean('calendar', '_')
    build_latex_ordo(year)

 # todo use os to get a list of the dioceses or regions needed to complete an ordo

app(year=2022, diocese="roman")
