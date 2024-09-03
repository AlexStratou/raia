# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com
Licence: MIT

"""
from .rgb import *
from .emoji import *
__version__ = '0.3.0'


for name in defaults.keys():
    # Make Color objects through the dictionary
    locals()[name] = Color(*defaults[name])

    # Make backgrounds
    name_bg = name + '_bg'
    locals()[name_bg] = Color(*defaults[name], as_background=True)

for st in styles.keys():
    locals()[st.capitalize()] = Style(st)
