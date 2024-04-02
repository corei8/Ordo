from ordotools.tools.liturgical_dates import integer_to_roman
from ordotools.tools.parts import PENTECOST_MASSES


class TemporalData:

    def __init__(self):
        self.easy_data = {
            "Circumcision": {
                "code": "Circumcision" ,
                "rank": [3, "d II cl"],
                "color": "white",
                "mass": {"int": "Puer natus", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8_Stephen": {
                "code": "8_Stephen",
                "rank": [20, "s"],
                "color": "white",
                "mass": {"int": "Sederunt", "glo": True, "cre": False, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8_John": {
                "code": "8_John",
                "rank": [20, "s"],
                "color": "red",
                "mass": {"int": "Introit", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8_Innocents": {
                "code": "8_Innocents",
                "rank": [20, "s"],
                "color": "red",
                "mass": {"int": "Ex ore infantium", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "SNameJesus": {
                "code": "SNameJesus",
                "rank": [10, "d II cl"],
                "color": "white",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            # FIX: test this
            "SNameJesu_8_Ste": {
                "code": "SNameJesu_8_Ste",
                "rank": [10, "d II cl"],
                "color": "white",
                "mass": {"int": "In nomine Jesu", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com": [],
                # TODO: figure out what we have to do for this...
                "com": [{"feast": "S Stephani",}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            # Epiphany Season
            "V_Epiphany": {
                "code": "V_Epiphany",
                "rank": [12, "sd Vig privil 2 cl"],
                "color": "purple",
                "mass": {"int": "Dum medium silentium", "glo": True, "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "Epiphany": {
                "code": "Epiphany",
                "rank": [2, "d I cl cum Oct privil 2 ord"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8_Epiphany": {
                "code": "8_Epiphany",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (3, 2, 6, 1, 3, 0), # TODO: what is the solemnity?
                "fasting": False,
            },
            "D_Epiphany": {
                "code": "D_Epiphany",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "et Comm de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            # Holy Family
            "HolyFamily": {
                "code": "HolyFamily",
                "rank": [11, "dm"],
                "color": "white",
                "mass": {"int": "Exultat", "glo": True, "cre": True, "pre": "et communcantes de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "D_HolyFamily": {
                "code": "D_HolyFamily",
                "rank": [11, "dm"],
                "color": "white",
                "mass": {"int": "In excelso", "glo": True, "cre": True, "pre": "et Comm de Epiphania"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            ##      if x == "I in Quadragesima":

            # Ash Wednesday and the follwing
            "de_AshWed": {
                "code": "de_AshWed",
                "rank": [3, "s I cl"],
                "color": "purple",
                "mass": {"int": "Misereris", "glo": True, "cre": True, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "AshWed_f5": {
                "code": "AshWed_f5",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Dum clamarem", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "AshWed_f6": {
                "code": "AshWed_f6",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Audivit", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "AshWed_fs": {
                "code": "AshWed_fs",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Audivit", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            "D_Lent_1": {
                "code": "D_Lent_1",
                "rank": [1, "sd I cl"],
                "color": "purple",
                "mass": {"int": "Invocabit me", "glo": False, "cre": True, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            # Ember days in Lent
            "Ember_Lent_4": {
                "code": "Ember_Lent_4",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Reminiscere", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "Ember_Lent_6": {
                "code": "Ember_Lent_6",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "De necessitatibus", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "Ember_Lent_s": {
                "code": "Ember_Lent_s",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Intret", "glo": False, "cre": False, "pre": "de Quadragesima"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            "SevenSorrows": {
                "code": "SevenSorrows",
                "rank": [14, "dm"],
                "color": "purple",
                "mass": {"int": "Stabant", "glo": False, "seq": "Stabat Mater", "cre": True, "pre": "de B. Maria Virg."},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            # Holy Week Ferias:
            # TODO: check the verbose rank
            "de_Palm_f2": {
                "code": "de_Palm_f2",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Judica, Domine", "glo": False, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (9, 2, 6, 13, 1, 0,),
                "fasting": True,
            },
            "de_Palm_f3": {
                "code": "de_Palm_f3",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "Nos autem", "glo": False, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (9, 2, 6, 13, 1, 0,),
                "fasting": True,
            },
            "de_Palm_f4": {
                "code": "de_Palm_f4",
                "rank": [3, "s"],
                "color": "purple",
                "mass": {"int": "In nomine Jesu", "glo": False, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            # Triduum:
            "de_Palm_f5": {
                "code": "de_Palm_f5",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Nos autem", "glo": True, "cre": False, "pre": "de Cruce"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "de_Palm_f6": {
                "code": "de_Palm_f6",
                "rank": [2, "d I cl"],
                "color": "black",
                "mass": {"int": "Haec dicit", "glo": False, "cre": False, "pre": ""},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "de_Palm_fs": {
                "code": "de_Palm_fs",
                "rank": [2, "d I cl"],
                "color": "purple",
                "mass": {"int": "In Missa", "glo": True, "cre": False, "pre": "Te quidem"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            # Easter Week TODO: Easter Vespers:
            "Easter": {
                "code": "Easter",
                "rank": [1, "d I cl cum Oct privil I ord"],
                "color": "white",
                "mass": {"int": "Ressurexi", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8Easter_f2": {
                "code": "8Easter_f2",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Introduxit", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8Easter_f3": {
                "code": "8Easter_f3",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Aqua sapientiae", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8Easter_f4": {
                "code": "8Easter_f4",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Venite", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8Easter_f5": {
                "code": "8Easter_f5",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Victricem", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hang Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8Easter_f6": {
                "code": "8Easter_f6",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Eduxit eos", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "WhitSaturday": {
                "code": "WhitSaturday",
                "rank": [3, "sd"],
                "color": "white",
                "mass": {"int": "Eduxit Dominus", "glo": True, "seq": "Victimae paschali laudes", "cre": True, "pre": "et Comm et Hanc Igitur, ut in die Paschae"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            # Solemnity of St. Joseph  TODO: add the octave
            "StJoseph": {
                "code": "StJoseph", #, C. et Ecclesiæ Universalis Patroni",
                "rank": [2, "d I cl cum Oct Communi"],
                "color": "white",
                "mass": {"int": "Justus ut palma", "glo": True, "cre": True, "pre": "de S Joseph"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (1, 2, 4, 4, 1, 0),
                "fasting": False,
            },
            "8_StJoseph": {
                "code": "8_StJoseph",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Missa", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            # Rogation Days
            "Rogation_1": {
                "code": "Rogation_1",
                "rank": [19, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 13, 0, 0,),
                "fasting": False,
            },
            "Rogation_2": {
                "code": "Rogation_2",
                "rank": [23, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 13, 0, 0,),
                "fasting": False,
            },
            "Rogation_3": {
                "code": "Rogation_3",
                "rank": [23, "feria"],
                "color": "purple",
                "mass": {"int": "Exaudivit", "glo": False, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0,),
                "fasting": False,
            },


            # Ascension
            "Ascension": {
                "code": "Ascension",
                "rank": [2, "d I cl cum Oct privil 3 ord"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8_Ascension": {
                "code": "8_Ascension",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (3, 2, 3, 1, 3, 0),
                "fasting": False,
            },

            "p_Ascension_f6": {  # TODO: this day has special rules
                "code": "p_Ascension_f6",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Viri Galilæi", "glo": True, "cre": True, "pre": "et Comm de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            ##  }
            ##      )
            ##      ascension_day = easter(year) + week(i) + indays(5)
            ##      if x == "Dominica infra Octavam Ascensionis":
            ##      for j, y in enumerate(ROMANS[1: 6], start=1):
            ##      if ascension_day + indays(j) == easter(year) + week(i):
            ##      continue
            ##      elif (ascension_day + indays(j)).strftime("%A") == "Saturday":

            # TODO: see if this is right
            "D_Ascension": {
                "code": "D_Ascension",
                "rank": [16, "sd"], # FIX: check the rank and the Introit
                "color": "white",
                "mass": {"int": "Exaudi, Domine", "glo": True, "cre": False, "pre": "de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (5, 1, 6, 13, 3, 0,),
                "fasting": False,
            },

            "S_8_Ascension": {
                "code": "S_8_Ascension",
                "rank": [17, "sd"],
                "color": "white",
                "mass": {"int": "Exaudi, Domine", "glo": True, "cre": False, "pre": "de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            "WhitSunday": {
                "code": "WhitSunday",
                "rank": [1, "dm I cl"],
                "color": "white",
                "mass": {"int": "Quasi modo", "glo": True, "cre": True, "pre": "Paschalis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,

            },

            "V_Pentecost": {
                "code": "V_Pentecost",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "red",
                "mass": {"int": "Cum sanctificatus", "glo": True, "cre": False, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            # Pentecost Week
            "Pentecost": {
                "code": "Pentecost",
                "rank": [1, "d I cl cum Oct privil I ord"],
                "color": "red",
                "mass": {"int": "Spiritus Domini", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            # TODO: see if the first two ferias are 2 or 3
            "8Pent_f2": {
                "code": "8Pent_f2",
                "rank": [3, "d I cl"],
                "color": "red",
                "mass": {"int": "Cibavit eos", "glo": True, "cre": True, "seq": "Veni, Sancte Spiritus", "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8Pent_f3": {
                "code": "8Pent_f3",
                "rank": [3, "d I cl"],
                "color": "red",
                "mass": {"int": "Cibavit eos", "glo": True, "cre": True, "seq": "Veni, Sancte Spiritus", "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8Pent_f5": {
                "code": "8Pent_f5",
                "rank": [3, "d I cl"],
                "color": "red",
                "mass": {"int": "Accepite jucunditatem", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            "Ember_Pent_4": {
                "code": "Ember_Pent_4",
                "rank": [3, "sd"],
                "color": "red",
                "mass": {"int": "Deus, dum egredereris", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "Ember_Pent_6": {
                "code": "Ember_Pent_6",
                "rank": [3, "sd"],
                "color": "red",
                "mass": {"int": "Repleatur os meum", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "Ember_Pent_s": {
                "code": "Ember_Pent_s",
                "rank": [3, "sd"],
                "color": "red",
                "mass": {"int": "Caritas Dei", "glo": True, "seq": "Veni, Sancte Spiritus", "cre": True, "pre": "et Comm et Hanc Igitur de Pentecoste"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            # First three post-Pentecost Sundays
            "Trinity": {
                "code": "Trinity",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Benedicta sit", "glo": True, "cre": True, "pre": "de Ssma Trinitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "D_Pent_2": {
                "code": "D_Pent_2", #Christi (Dominica II post Pentecosten)",
                "rank": [12, "sd"],
                "color": "green",
                "mass": {"int": "Factus est", "glo": True, "seq": "Lauda, Sion, Salvatorem", "cre": True, "pre": "de Nativitate, vel de Ssma Trinitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "D_Pent_3": {
                "code": "D_Pent_3",  # (Dominica III post Pentecosten)",
                "rank": [12, "sd"],
                "color": "green",
                "mass": {"int": "Respice in me", "glo": True, "cre": True, "pre": "de sacratissimo Code Jesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            "CorpusChristi": {
                "code": "CorpusChristi",
                "rank": [2, "d I cl cum Oct privil 2 ord"],
                "color": "white",
                "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            "8_CorpusChristi": {
                "code": "8_CorpusChristi",
                "rank": [4, "dm"],
                "color": "white",
                "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            "SacredHeart": {
                "code": "SacredHeart",
                "rank": [2, "d I cl cum Oct privil 3 ord"],
                "color": "white",
                "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (1, 0, 3, 1, 1, 0),
                "fasting": False,
            },

            "8_SacredHeart": {
                "code": "8_SacredHeart",
                "rank": [13, "dm"],
                "color": "white",
                "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            "Ember_Sept_4": {
                "code": "Ember_Sept_4",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Exsultate Deo", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            "Ember_Sept_6": {
                "code": "Ember_Sept_6",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Laetetur cor", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "Ember_Sept_s": {
                "code": "Ember_Sept_s",
                "rank": [19, "s"],
                "color": "purple",
                "mass": {"int": "Venite, adoremus", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },

            # Christ the King
            "ChristKing": {
                "code": "ChristKing",
                "rank": [2, "d I cl"],
                "color": "white",
                "mass": {"int": "Dignus est", "glo": True, "cre": True, "pre": "de DNJC Rege"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            # Ember Days of Advent
            "Ember_Advent_4": {
                "code": "Ember_Advent_4",
                "rank": [19, "feria"], # TODO: check the rank for this
                "color": "purple",
                "mass": {"int": "Rorate cæli", "glo": False, "cre": False, "pre": "Communis"},
                "com": [{"oration": "Deus qui de beate"}, {"oration": "Ecclesiæ"}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },
            "Ember_Advent_6": {
                "code": "Ember_Advent_6",
                "rank": [19, "feria"], # TODO: check the rank for this
                "color": "purple",
                "mass": {"int": "Prope es tu", "glo": False, "cre": False, "pre": "Communis"},
                "com": [{"oration": "Deus qui de beate"}, {"oration": "Ecclesiæ"}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },
            "Ember_Advent_s": {
                "code": "Ember_Advent_s",
                "rank": [19, "feria"],  # TODO: check the rank for this
                "color": "purple",
                "mass": {"int": "Veni, et ostende", "glo": False, "cre": False, "pre": "Communis"},
                "com": [{"oration": "Deus qui de beate"}, {"oration": "Ecclesiæ"}],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": True,
            },


            # Christmastide
            "V_Christmas": {
                "code": "V_Christmas",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "purple",
                "mass": {"int": "Hodie scietis", "glo": False, "cre": False, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": True,
            },
            "DV_Christmas": {
                "code": "DV_Christmas",
                "rank": [3, "d I cl Vig privil I cl"],
                "color": "purple",
                "mass": {"int": "Hodie scietis", "glo": False, "cre": True, "pre": "de Trinitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "Christmas": {
                "code": "Christmas",
                "rank": [2, "d I cl cum Oct privil 3 ord"],
                "color": "white",
                "mass": {
                    "Ad Primam Missam": {"int": "Domine dixit", "glo": True, "cre": True, "pre": r'et Comm (in hac Missa tantum dicitur "noctem") de Nativitate'},
                    "Ad Secundam Missam": {"int": "Lux fulgebit", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                    "Ad Tertiam Missam": {"int": "Puer natus", "glo": True, "cre": True, "pre": "et Comm de Nativitate", "proper_last_gospel": "Epiph"},
                },
                "matins": {},
                "lauds": {"psalms": "sunday"},
                "prime": {"v_r": "Qui natus es"},
                "little_hours": {"psalms": "sunday"},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {"sunday": True,},
                "office_type": "festiva",
                "nobility": (1, 1, 3, 1, 1, 0),
                "fasting": False,
            },
            "D_Christmas_r": {
                "code": "D_Christmas_r",
                "rank": [12, "sd"],
                "color": "white",
                "mass": {"int": "Dum medium silentium", "glo": True, "cre": True, "pre": "de Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "D_Christmas": {
                "code": "D_Christmas",
                "rank": [12, "sd"],
                "color": "white",
                "mass": {"int": "Dum medium", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "dominica",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "8_Chritmas_f6": {
                "code": "8_Chritmas_f6",
                "rank": [16, "sd"],
                "color": "white",
                "mass": {"int": "Puer natus est nobis", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""}, "office_type": "feria",
                "compline": {},
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "StStephan": {
                "code": "StStephan",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "red",
                "mass": {"int": "Sederunt", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "StJohn": {
                "code": "StJohn",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "white",
                "mass": {"int": "In medio ecclesiæ", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "StsInnocents": {
                "code": "StsInnocents",
                "rank": [10, "d II cl cum Oct simplici"],
                "color": "red",
                "mass": {"int": "Ex ore infantium", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "StThomas": {
                "code": "StThomas",
                "rank": [15, "d"],
                "color": "red",
                "mass": {"int": "Gaudeamus omnes", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "StSylvester": {
                "code": "StSylvester",
                "rank": [15, "d"],
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": False, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },

            # TEST:
            "D_StThomas": {
                "code": "D_StThomas",
                "rank": [15, "d"],
                "color": "red",
                "mass": {"int": "Gaudeamus omnes", "glo": True, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            "D_StSylvester": {
                "code": "D_StSylvester",
                "rank": [15, "d"],
                "color": "white",
                "mass": {"int": "Si diligis me", "glo": False, "cre": True, "pre": "et Comm de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (0, 0, 0, 0, 0, 0,),
                "fasting": False,
            },
            # TODO: add the Sundays if the fall on St. Thomas or St. Sylvester
        }

        self.data = self.easy_data |\
            self.epiphany_time() |\
            self.epiphany_octave() |\
            self.septuagesima_time() |\
            self.lent_sundays() |\
            self.paschaltime() |\
            self.ascension_ferias() |\
            self.corpus_ferias() |\
            self.sacredheart_ferias() |\
            self.solemnity_st_joseph() |\
            self.pentecost_sundays() |\
            self.pentecost_epiphany_sundays() |\
            self.last_pentecost() |\
            self.advents() |\
            self.three_weeks_after_pentecost()

    def lent_sundays(self) -> dict:
        the_days = {}
        normal_lents = [f"D_Lent_{l+1}" for l in range(4)]
        later_lents = ["D_Passion_5", "D_Palm_6"]
        lents = [*normal_lents, *later_lents]
        rank = 8
        for x, date in enumerate(lents):
            if x in [0, 1, 3]:
                rank = 1
            else:
                rank = 8
            for feria in range(7):
                if feria == 0:
                    the_days |= {
                        date: {
                            "code": date,
                            "rank": [rank, "sd I cl"],  # FIX: check this
                            "color": f"{'purple' if x+1 != 4 else 'pink'}",
                            "mass": {
                                "int": "",  # TODO: add all of the Introits
                                "glo": False,
                                "cre": False,
                                "pre": "de Quadragesima" if x < 6 else "de Cruce",
                            },
                            "matins": {},
                            "lauds": {},
                            "prime": {},
                            "little_hours": {},
                            "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                            "compline": {},
                            "office_type": False,
                            "nobility": (0, 0, 0, 0, 0, 0,),
                            "fasting": False,
                        }
                    }
                else:
                    the_days |= {
                        f"de_{'Lent' if x < 4 else 'Passion'}_f{feria+1 if feria != 6 else 's'}": {
                            # "code": f"Feria {integer_to_roman(feria+1)} infra Hebd {integer_to_roman(x+1)} in Quadragesima",
                            "code": f"de_{'Lent' if x < 4 else 'Passion'}_f{feria+1 if feria != 6 else 's'}",
                            "rank": [19, "feria"],
                            "color": "purple",
                            "mass": {
                                "int": "", # TODO: add all of the Lent feria Introits
                                "glo": False,
                                "cre": False,
                                "pre": "de Quadragesima" if x < 6 else "de Cruce",
                            },
                            "matins": {},
                            "lauds": {},
                            "prime": {},
                            "little_hours": {},
                            "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                            "compline": {},
                            "office_type": False,
                            "nobility": (9, 2, 6, 13, 3, 0), # FIX: Lent has higher ranking ferias?
                            "fasting": True,
                        }
                    }
        return the_days

    def ascension_ferias(self) -> dict:
        return { # NOTE: there are duplicates, but does it matter?
            f"in_8_Ascension_{date}": {
                "code": f"in_8_Ascension_{date}",
                "rank": [16, "sd"],
                "color": "white",
                "mass": {"int": "Viri galilæi", "glo": True, "cre": False, "pre": "de Ascensione"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": False,
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": False,
            } for date in range(1,8)
        }

    def corpus_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_CorpusChristi": {
                "code": f"{date+1}_in_8_CorpusChristi",
                "rank": [9, "feria"],
                "color": "white",
                "mass": {"int": "Cibavit eos", "glo": True, "seq": "Lauda, Sion", "cre": True, "pre": "de Nativitate"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (9, 2, 6, 13, 3, 0),
                "fasting": False,
            } for date in range(1,8)
        }

    def sacredheart_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_SacredHeart": {
                "code": f"{date+1}_in_8_SacredHeart",
                "rank": [18, "sd"], # TODO: verify this rank
                "color": "white",
                "mass": {"int": "Cogitationes", "glo": True, "cre": True, "pre": "de Ssmo Corde Iesu"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "festiva",
                "nobility": (1, 0, 3, 1, 1, 0),
                "fasting": False,
            } for date in range(1,8)
        }


    def pentecost_sundays(self) -> dict:
        # TODO: add the first 4 Sundays after Pentecost (excluding Trinity)
        pentecost_season = {}
        for date in range(4, 29):
            pentecost_season |= {
                f"D_Pent_{date}": {
                    "code": f"D_Pent_{date}",
                    "rank": [12, "sd"],
                    "color": "green",
                    "mass": {"int": f"{PENTECOST_MASSES[date-5] if date >= 4 else ''}", "glo": True, "cre": True, "pre": "de Trinitate"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (0, 0, 0, 0, 0, 0,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                pentecost_season |= {
                    f"de_Pent_{date}_f{feria+2 if feria != 5 else 's'}": {
                        "code": f"de_Pent_{date}_f{feria+2 if feria != 5 else 's'}",
                        "rank": [23, "sd"],
                        "color": "green",
                        "mass": {"int": f"{PENTECOST_MASSES[date-5] if date >= 4 else ''}", "glo": True, "cre": False, "pre": "Communi"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return pentecost_season

    def pentecost_epiphany_sundays(self) -> dict:
        """
        This is really rough and might not be too efficient, but 
        it works for now.
        """
        epiphany_pents = {}
        for pent in range(22,29):
            for epiph in range(3,7):
                epiphany_pents |= {
                    f"D_Epiph_{epiph}_{pent}": {
                        "code": f"D_Epiph_{epiph}_{pent}",
                        "rank": [12, "sd"],
                        "color": "green",
                        "mass": {"int": "Dicit Dominus", "glo": True, "cre": True, "pre": "de Trinitate"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (0, 0, 0, 0, 0, 0,),
                        "fasting": False,
                    }
                }
                for feria in range(6):
                    epiphany_pents |= {
                        f"de_Epiph_{epiph}_{pent}_f{feria+2 if feria != 5 else 's'}": {
                            "code": f"de_Epiph_{epiph}_{pent}_f{feria+2 if feria != 5 else 's'}",
                            "rank": [23, "feria"],
                            "color": "green",
                            "mass": {"int": "Dicit Dominus", "glo": True, "cre": False, "pre": "Communi"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                            "matins": {},
                            "lauds": {},
                            "prime": {},
                            "little_hours": {},
                            "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                            "compline": {},
                            "office_type": "dominica",
                            "nobility": (9, 2, 6, 13, 3, 0),
                            "fasting": False,
                        }
                    }
        return epiphany_pents

    def last_pentecost(self) -> dict:
        last_pents = {}
        for pent in range(23, 29):
            last_pents |= {
                f"D_UltPent_{pent}": {
                    "code": f"D_UltPent_{pent}",
                    "rank": [12, "sd"],
                    "color": "green",
                    "mass": {"int": PENTECOST_MASSES[-1], "glo": True, "cre": True, "pre": "de Trinitate"},
                    "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (0, 0, 0, 0, 0, 0,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                last_pents |= {
                    f"de_UltPent_{pent}_f{feria+2 if feria != 5 else 's'}": {
                        "code": f"de_UltPent_{pent}_f{feria+2 if feria != 5 else 's'}",
                        "rank": [12, "sd"], # FIX: fix the rank
                        "color": "green",
                        "mass": {"int": PENTECOST_MASSES[-1], "glo": True, "cre": False, "pre": "Communi"},
                        "com": [{"oration": "A cunctis", }, {"oration": "ad libitum", },],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return last_pents

    def advents(self) -> dict:
        advent_season = {}
        advent_sundays = [
            "Ad te levavi",
            "Populus Sion",
            "Gaudete",
            "Rorate cæli",
        ]
        for x, introit in enumerate(advent_sundays):
            advent_season |= {
                f"D_Advent_{x+1}": { # TODO: verify that 2-4 advents are minor sundays
                                    "code": f"D_Advent_{x+1}",
                                    "rank": [1 if x == 0 else 12, f"{'sd I cl' if x == 0 else 'sd II cl'}"],
                                    "color": f"{'purple' if x+1 != 3 else 'pink'}",
                                    "mass": {"int": f"{introit}", "glo": False, "cre": True, "pre": "de Trinitate"},
                                    "com": [{"oration": "Deus qui de beate"},{"oration": "Ecclesiæ"}],
                                    "matins": {},
                                    "lauds": {},
                                    "prime": {},
                                    "little_hours": {},
                                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                                    "compline": {},
                                    "office_type": "dominica",
                                    "nobility": (0, 0, 0, 0, 0, 0,),
                                    "fasting": False,
                                    }
            }
            for feria in range(6):
                advent_season |= {
                    f"Advent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "code": f"Advent_{x+1}_f{feria+2 if feria != 5 else 's'}",
                        "rank": [23, "feria"], # FIX: change the rank
                        "color": "purple",
                        "mass": {"int": f"{introit}", "glo": False, "cre": True, "pre": "de Trinitate"},
                        "com": [{"oration": "Deus qui de beate"},{"oration": "Ecclesiæ"}],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "feria",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return advent_season

    def three_weeks_after_pentecost(self) -> dict:
        # NOTE: this is overkill, but it works, and is probably faster than a fix
        weeks = {}
        introits = [
            "Benedicta sit",
            "Factus est",
            "Respice in me",
        ]
        for x, introit in enumerate(introits):
            for feria in range(6):
                weeks |= {
                    f"de_Pent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "code": f"de_Pent_{x+1}_f{feria+2 if feria != 5 else 's'}",
                        "rank": [23, "feria"], # FIX: change the ranking
                        "color": "green", # TODO: check if this is right of the Trinity
                        "mass": {"int": introit, "glo": True, "seq": "Lauda, Sion, Salvatorem", "cre": False, "pre": "de Trinitate"},
                        "com": [],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "ferial",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    },
                }
        return weeks

    def paschaltime(self) -> dict:
        paschaltime = {}
        for week in range(6):
            paschaltime |= {
                f"D_Easter_{week+1}": {
                    "code": f"D_Easter_{week+1}",
                    "rank": [12, "sd"],
                    "color": "white",
                    "mass": {"int": "Missa", "glo": True, "cre": True, "pre": "Communis"},
                    "com": [], # FIX: easter preface?
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (0, 0, 0, 0, 0, 0,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                pass
                paschaltime |= {
                    f"de_Easter_{week+1}_f{feria+2 if feria != 5 else 's'}": {
                        "code": f"de_Easter_{week+1}_f{feria+2 if feria != 5 else 's'}",
                        "rank": [23, "feria"], # FIX: check the ranking
                        "color": "white",
                        "mass": {"int": "Missa", "glo": True, "cre": False, "pre": "Communis"},
                        "com": [], # FIX: easter preface?
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "feria",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return paschaltime

    def solemnity_st_joseph(self) -> dict:
        solemnity_ferias = {}
        for feria in range(6):
            solemnity_ferias |= {
                f"{feria+2}_in_8_StJoseph": {
                    "code": f"{feria+2}_in_8_StJoseph",
                    "rank": [18, "feria"], # FIX: check the verbose rank
                    "color": "white",
                    "mass": {"int": "Justus ut palma", "glo": True, "cre": True, "pre": "de S Joseph"},
                    "com": [],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": False,
                    "nobility": (9, 2, 6, 13, 3, 0),
                    "fasting": False,
                }
            }
        return solemnity_ferias

    def septuagesima_time(self) -> dict:
        septuagesima = {}
        for x, sunday in enumerate(["Septuagesima", "Sexagesima", "Quinquagesima"]):
            septuagesima |= {
                sunday: {
                    "code": sunday,
                    "rank": [8, "sd II cl"],
                    "color": "purple",
                    "mass": {"int": "", "glo": False, "cre": True, "pre": "Communis"},
                    "com": [], # FIX: preface
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (0, 0, 0, 0, 0, 0,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                septuagesima |= {
                    f"de_{sunday[:4]}_f{feria+2 if feria != 5 else 's'}": {
                        "code": f"de_{sunday[:4]}_f{feria+2 if feria != 5 else 's'}",
                        "rank": [23, "feria"],
                        "color": "purple",
                        "mass": {"int": "", "glo": False, "cre": True, "pre": "Communis"},
                        "com": [], # FIX: preface
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "dominica",
                        "nobility": (9, 2, 6, 13, 3, 0),
                        "fasting": False,
                    }
                }
        return septuagesima

    def epiphany_time(self) -> dict:
        epiphany = {}
        for sunday in range(6):
            epiphany |= {
                f"D_Epiph_{sunday+1}": {
                    "code": f"D_Epiph_{sunday+1}",
                    "rank": [12, "sd"],
                    "color": "green",
                    "mass": {"int": "Omnis terra", "glo": True, "cre": True, "pre": "de Ssma Trinitate"},
                    "com": [],  # FIX: introit
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "dominica",
                    "nobility": (0, 0, 0, 0, 0, 0,),
                    "fasting": False,
                }
            }
            for feria in range(6):
                epiphany |= {
                    f"de_Epiph_{sunday+1}_{feria+2 if feria != 5 else 's'}": {
                        "code": f"de_Epiph_{sunday+1}_{feria+2 if feria != 5 else 's'}",
                        "rank": [23, "feria"],
                        "color": "white",
                        "mass": {"int": "Omnis terra", "glo": True, "cre": False, "pre": "Communis"},
                        "com": [],
                        "matins": {},
                        "lauds": {},
                        "prime": {},
                        "little_hours": {},
                        "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                        "compline": {},
                        "office_type": "feria",
                        "nobility": (8, 2, 6, 13, 3, 0,),
                        "fasting": False,
                    }
                }
        return epiphany

    def epiphany_octave(self) -> dict:
        octave = {
            "8_Epiph_fs": {
                "code": "8_Epiph_fs",
                "rank": [9, "feria"],
                "color": "white",
                "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                "com": [],
                "matins": {},
                "lauds": {},
                "prime": {},
                "little_hours": {},
                "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                "compline": {},
                "office_type": "feria",
                "nobility": (8, 2, 6, 13, 3, 0,), # FIX: check this rank
                "fasting": False,
            },
        }
        for feria in range(6):
            octave |= {
                f"8_Epiph_f{feria+2}": {
                    "code": f"8_Epiph_f{feria+2}",
                    "rank": [9, "feria"],
                    "color": "white",
                    "mass": {"int": "Ecce advenit", "glo": True, "cre": True, "pre": "Communis"},
                    "com": [],
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": {"proper": False, "admag": ["firstVespers", "secondVespers"], "propers": {}, "oration": ""},
                    "compline": {},
                    "office_type": "feria",
                    "nobility": (8, 2, 6, 13, 3, 0,), # FIX: check this rank
                    "fasting": False,
                }
            }
        return octave
