import subprocess
from datetime import datetime
import os
import importlib
from tools.feast import Feast
from tools.helpers import latex_replacement, translate_month


def build_latex_ordo(year, mdl: dict):
    """ build an ordo booklet in 8.5 by 5.5 """
    # try:
    #     mdl = importlib.import_module('calen.calendar_' + str(year)).calen
    # except AttributeError:
    #     pass
    # else:
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
\usepackage{gregoriosyms} % for the versicle and response symbols
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
                if x.strftime("%m").lstrip() == str(i):
                    feast = Feast(x, mdl[x])
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
                \begin{justify}''' + feast.office_type2latex + 
                feast.display_matins_as_latex +
                feast.display_lauds_as_latex +
                feast.display_little_hours_as_latex +
                feast.display_prime_as_latex +
                latex_replacement(feast.display_mass_as_latex()) +
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
        subprocess.run(
            'lualatex '+file+' -interaction nonstopmode',
            shell=True,
            # stdout=subprocess.DEVNULL
        )
        # TODO: move the pdf into a seperate directory and overwrite the old one
        os.chdir(working_dir)
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


def build_test_website(year: int, y: dict) -> None:

    # build the calendar with blank days
    cal = []
    for x in range(54):
        cal.append([])
        for d in range(7):
            cal[x].append([])

    # %U' is the week number with Sunday being the first day of the week
    # %w' is the weekday number with Sunday as the first day of the week

    # Add the data for each day at the beginning
    for date in y.keys():
        placement = int(date.strftime('%U'))
        cal[placement][int(date.strftime('%w'))] = [
            y[date],
            date.strftime("%B"),
            date.strftime("%d")
        ]

    # determine the file output and starter text depending on the calendar
    build_dirs = [
        "./output/ordosite/_includes/calendar.html",  # for the Jekyll site
        "./output/html/index.html"                    # for quick reference
    ]
    last_week = False

    for out, path in enumerate(build_dirs):
        with open(path, 'w') as f:
            f.truncate(0)

            # NOTE: might not be necessary anymore
            if out == 1:
                f.write("""
<!DOCTYPE html>
<html lang=""en-us">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta charset="utf-8">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/\
bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2\
FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
<style>body {background: aliceblue;}</style>
<title>test site</title>
</head>
<body>
                """)
            f.write('<div class="container center p-0">')

            # useful variables
            month_memory = ''
            weekdays = """
<div class="row w-100 m-0 rounded-top bg-primary">
<div class="col bg-primary text-white p-1 text-center rounded"> Sunday </div>
<div class="col bg-primary text-white p-1 text-center"> Monday </div>
<div class="col bg-primary text-white p-1 text-center"> Tuesday </div>
<div class="col bg-primary text-white p-1 text-center"> Wednesday </div>
<div class="col bg-primary text-white p-1 text-center"> Thursday </div>
<div class="col bg-primary text-white p-1 text-center"> Friday </div>
<div class="col bg-primary text-white p-1 text-center rounded"> Saturday </div>
</div>
            """

            def close_div():
                return '</div>'

            def start_row(classes=''):
                return f'<div class="row w-100 m-0 {classes}">'

            def start_col(classes=''):
                return f'<div class="col col-h p-1 text-break {classes}">'

            def empty_col(classes=''):
                return start_col(classes)+close_div()

            def build_month(month, cols, file, year=year) -> None:
                file.write('<section>')
                file.write(start_row())  # starts the month row
                file.write(f'''
                <div class="mt-3 text-start">
                    <h3 class="pt-1">
                        {month} {year}
                    </h3>
                </div>
                ''')
                file.write(close_div())  # closes the month row
                file.write(f'{weekdays}')
                file.write(start_row('border empty_dates'))
                file.write(empty_col()*cols)
                return None

            for j, aweek in enumerate(cal):

                # See if it is the last week of the year
                if last_week is True:
                    break
                elif j+1 == len(cal):
                    last_week = True
                else:
                    pass

                for i, aday in enumerate(aweek):

                    # alternate the cell shading
                    if i % 2 == j % 2:
                        shading = 'bg-body'
                    else:
                        shading = 'bg-light'

                    # see if the day is a calendar day
                    if len(aday) == 2:
                        index = 0  # the day is not a calendar day
                    elif len(aday) == 0:
                        continue
                    else:
                        index = 1

                    # How to treat the beginning of a month
                    if aday[index] != month_memory:  # if we have a new month
                        if j == 1 and i != 0:
                            pass
                        elif j == 1 and i == 0:
                            pass
                        else:
                            if j == 0:
                                f.write('<section>')
                            else:
                                f.write(empty_col()*int(7-i))
                                f.write(close_div())
                                f.write('</section>')
                        build_month(month=aday[index], cols=i, file=f)
                    else:
                        if i == 0 and j != 0:
                            f.write(start_row('border empty_dates'))

                    month_memory = aday[index]

                    f.write(start_col(
                        f'fw-light d-flex flex-column\
                        justify-content-between {shading}'
                    ))

                    # date-bar
                    f.write(f'<div class="w-100 p-1">\
                    {aday[-1].lstrip("0")}</div>')

                    # feast
                    f.write(f'''
                    <div class="text-center smaller-text w-100">
                    {'<h1>🧐</h1>' if index != 1 else aday[0]['feast']}
                    </div>
                    ''')

                    # statusbar helpers
                    if out == 1:
                        fish_path = "assets/images/full_fish.png"
                    else:
                        fish_path = "/assets/images/full_fish.png"
                    color = aday[0]["color"]
                    blank_image = "data:image/gif;base64,R0lGODlhAQABAIAAAP///\
                    wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="
                    fish_placeholder = f'<img src="\
                    {blank_image}\
                    " height="16em" width="16em">'

                    # build the "statusbar"
                    f.write(f'''
                    <div class="w-100 p-0 d-flex flex-column justify-content-between align-items-center">

                    { f'<div><small>{aday[0]["rank"][1]}</small></div>'}
                    <div class="text-end w-100 p-1 d-flex flex-row
                    justify-content-between align-items-end" height="16em">

                    { f'<img src="{blank_image}" height="16em" width="16em" style="border: solid 1px black; border-radius: 50%; background: {color}">'}

                    {f'<img src="{fish_path}" height="16em">' if aday[0]["fasting"] is True or i == 5 else fish_placeholder}

                    </div></div>
                    ''')

                    f.write("</div>")  # close the column

                    # add blank days if it is the last day
                    if last_week is True and aday[-1] == str(31):
                        f.write(empty_col()*int(6-i))
                        break

                f.write("</div>")  # close the row

            if out == 1:
                f.write("</section></div></div></body></html>")

            f.close()  # FIX: might not be necessary

        with open(path) as f:
            lines = list(f)
        with open(path, 'w') as out:
            for line in lines:
                out.write(line.lstrip())
            f.close()

    return None