import subprocess
from datetime import datetime
import os
import importlib
from ordo_tools.utils import latex_replacement, Feast, translate_month


def build_latex_ordo(year):
    """ build an ordo booklet in 8.5 by 5.5 """
    try:
        mdl = importlib.import_module('calen.calendar_' + str(year)).calen
    except AttributeError:
        pass
    else:
        mdldates = sorted(mdl)
        with open("output/latex/ordo_" + str(year) + ".tex", "a") as f:
            f.truncate(0)
            f.write(
                r'''
    % !TEX program = lualatex
    \documentclass[10pt, openany]{book}
    \title{Ordo '''+str(year)+r'''}
    \author{Roman Catholic Institute}
    \usepackage{ragged2e}
    \usepackage{gregoriotex} % for the versicle and response symbols
    \usepackage{microtype}
    \usepackage[T1]{fontenc}
    \usepackage{fontspec}
    \setmainfont[
        Path = /Library/Fonts/, 
        Extension = .ttf, 
        Ligatures = TeX, 
        BoldFont = Cardob101, 
        ItalicFont = Cardoi99,
        ]{Cardo104s}
    \usepackage[latin]{babel}
    \usepackage{geometry}
    \geometry{
        paperheight=8.5in, 
        paperwidth=5.5in, 
        left=1.0in, 
        right=1.0in, 
        top=1.0in, 
        bottom=1.0in,
        }
    \usepackage{anyfontsize}
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \renewcommand{\chaptermark}[1]{% 
        \markboth{#1}{}
        }
    \begin{document}
        % \maketitle
        % just something temporary for now
        \begin{titlepage}
            \begin{center}
                {\fontsize{50}{60}\selectfont \textsc{Ordo '''+str(year)+r'''}}
            \end{center}
            \begin{center}
                {\footnotesize \textsc{Roman Catholic Institute}}
            \end{center}
        \end{titlepage}
        \clearpage\begingroup\pagestyle{empty}\cleardoublepage\endgroup
    '''
            )
            for i in range(1, 13):
                month = datetime.strptime(
                    str(i)+'/1/'+str(year), '%m/%d/%Y').strftime('%B')
                _month = translate_month(month)
                # todo get rid of the chapter number
                f.write(
                    r'''
        \chapter{''' + _month + r'''}
                        ''')
                for x in mdldates:
                    if int(x.split('/')[0]) == i:
                        feast = Feast(x, mdl[x])
                        # todo #6 make the latin day of the week using FERIAS in temporal_cycle.py
                        # todo make the header of the last page of the previous month match the previous month
                        f.write(
                            r'''
        \begin{center}
            \begin{minipage}{3.5in}
                \vspace{2em}
                \begin{minipage}{0.5in}
                    {\Huge '''+latex_replacement(feast.feast_date_display)+r'''} \\
                    {\normalsize '''+feast.translate_weekday+r'''} \\
                    {\normalsize '''+feast.translate_color+r'''}
                \end{minipage}
                \begin{minipage}{3.0in}
                    \textbf{ \large '''+latex_replacement(feast.name)+r''' \\
                    \textnormal{\normalsize '''+feast.rank_v+r'''}} \\ ''' + latex_replacement(feast.com_in_title)+r'''
                \end{minipage}
                \begin{justify}'''+feast.office_type2latex+
                    feast.display_matins_as_latex + 
                    feast.display_lauds_as_latex +
                    feast.display_little_hours_as_latex +
                    feast.display_prime_as_latex +
                    latex_replacement(feast.display_mass_as_latex())+
                    feast.display_vespers_as_latex + 
                    feast.display_compline_as_latex +r'''
                \end{justify}
            \end{minipage}
        \end{center}
    ''')
            f.write("\n\end{document}")
        file = 'ordo_'+str(year)+'.tex'
        working_dir = os.getcwd()
        os.chdir('output/latex/')
        subprocess.run('lualatex '+file+' -interaction nonstopmode',
                    shell=True)#, stdout=subprocess.DEVNULL)
        os.chdir(working_dir)
    return None


def readme_calendar(year):
    try:
        mdl = importlib.import_module(
            'calen.calendar_' + str(year)).calen
    except AttributeError:
        pass
    else:
        mdldates = sorted(mdl)
        with open('README.md', 'a') as f:
            f.truncate(0)
            f.write(r'# Ordo')
            f.write(r'')
            f.write(r'Traditional Catholic Ordo for the United States, Australia, Canada and Nantes.')
            f.write(r'')
            f.write(r'Managed by the Roman Catholic Institute.')
            f.write(r'')
            f.write(r'## Python Specifications')
            f.write(r'')
            f.write(r'Python 3.x.x 64-bit')
            f.write(r'')
            f.write(r'### Modules:')
            f.write(r'')
            f.write(r'[dateutil](https://dateutil.readthedocs.io/en/stable/)')
            f.write(r'```bash')
            f.write(r'pip install python-dateutil')
            f.write(r'```')
            f.write(r'')
            f.write(r'## Overview')
            f.write(r'')
            f.write(r'The temporal cycle is generated by a funtion as a dictionary. The sanctoral cycle is made up of several files for country, region and diocese, and each file is a pre-built dictionary. These are combined with the temporal cycle after the latter is generated.')
            f.write(r'')
            f.write(r'The result is a dictionary containing:')
            f.write(r'')
            f.write(r'1. A liturgical calendar proper to an specified diocese (or several dioceses);')
            f.write(r'2. Indications of the peculiarities of the office of that day;')
            f.write(r'3. An ordo for the Mass of that day, or multiple Masses, if applicable.')
            f.write(r'')
            f.write(r"Easter is the first feast (every 'event' is treated as a feast) to be determined, since most of the liturgical year depends upon the date of Easter. Christmas, being static with regard to its date, requires that we only find the day of the week on which it falls. We begin building the temporal calendar with 01-01.")
            f.write(r'')
            f.write(r'## Progress')
            f.write(r'')
            f.write(r'- [x] Temporal Calendar')
            f.write(r'- [x] Combined Temporal and Sanctoral Calendar')
            f.write(r'- [ ] Masses')
            f.write(r'- [ ] Vespers')
            f.write(r'- [x] Colors of Mass and Office')
            f.write(r'- [ ] Lessons for Laudes')
            f.write(r'- [ ] Prime')
            f.write(r'- [ ] Little Hours')
            f.write(r'- [ ] US Calendar')
            f.write(r'- [ ] Australian Calendar')
            f.write(r'- [ ] Canadian Calendar')
            f.write(r'- [ ] Solemnities')
            f.write('\n\n')
            f.write('## Calendar for ' + str(year))
            f.write('\n\n')
            f.write('| Day | Date | Feast |')
            f.write('\n')
            f.write('|---|---|---|')
            f.write('\n')
            for x in mdldates:
                feast = Feast(x, mdl[x])
                f.write('| ' + feast.translate_weekday + ' | ' + feast.feast_date + ' | ' + feast.name + ' |')
                f.write('\n')
    return None


def build_latin_calendar(year) -> None:
    # todo make this calendar import work with a variable
    try:
        mdl = importlib.import_module('calen.calendar_' + str(year)).calen
    except AttributeError:
        pass
    else:
        mdldates = sorted(mdl)
        with open('output/latex_calendar/calendar_'+str(year)+'.tex', 'a') as f:
            f.truncate(0)
            f.write(
                r"""
    % !TEX program = lualatex
    \documentclass[10pt]{article}
    \usepackage{calendar_letter}
    \usepackage[landscape, letterpaper, margin=.25in]{geometry}
    \usepackage{palatino}
    \begin{document}
    \pagestyle{empty}
    \setlength{\parindent}{0pt}
    \StartingDayNumber=1
    """
            )
            for i in range(1, 13):
                blank_days = datetime.strptime(
                    str(i)+'/1/'+str(year), '%m/%d/%Y').strftime('%w')
                month = datetime.strptime(
                    str(i)+'/1/'+str(year), '%m/%d/%Y').strftime('%B')
                f.write(
                    r'''
    \begin{center}
        \textsc{\LARGE '''+month+r'''}\\ % Month
        % \textsc{\large Year} \\ % Year
    \end{center}
    \begin{calendar}{\textwidth}
    '''
                )
                for x in range(int(blank_days)):
                    f.write(
                        r'''
    \BlankDay
    '''
                    )
                f.write(r'''
    \setcounter{calendardate}{1}
    '''
                        )
                for x in mdldates:
                    if int(x.split('/')[0]) == i:
                        feast = Feast(x, mdl[x])
                        f.write(
                            r'''
    \day{'''+latex_replacement(feast.name)+r'''}{\vspace{1.5cm}}
    '''
                        )
                f.write(
                    r'''
    \finishCalendar
    \end{calendar}
    \pagebreak
    '''
                )
            f.write(
                r'''
    \end{document}
                '''
            )
        file = 'calendar_'+str(year)+'.tex'
        working_dir = os.getcwd()
        os.chdir('output/latex_calendar/')
        subprocess.run('lualatex '+file+' -interaction nonstopmode', shell=True)
        os.chdir(working_dir)
    return None
