# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:49:37 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

Module that instantiates some Color objects using a dictionary.
"""

from .rgb import Color

defaults = {
    # Dictionary with some default colors in RGB
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Red": (255, 0, 0),
    "Lime": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Silver": (192, 192, 192),
    "Gray": (128, 128, 128),
    "Maroon": (128, 0, 0),
    "Olive": (128, 128, 0),
    "Green": (0, 128, 0),
    "Purple": (128, 0, 128),
    "Teal": (0, 128, 128),
    "Navy": (0, 0, 128),
    "Orange": (255, 165, 0),
    "Brown": (165, 42, 42),
    "Pink": (255, 192, 203),
    "Gold": (255, 215, 0),
    "LightBlue": (173, 216, 230),
    "Violet": (238, 130, 238),
    "Indigo": (75, 0, 130),
    "Turquoise": (64, 224, 208),
    "Salmon": (250, 128, 114),
    "Beige": (245, 245, 220),
    "Lavender": (230, 230, 250)
}

__all__ = ['defaults']  # What to import using *
for name in defaults.keys():
    # Make Color objects through the dictionary
    __all__.append(name)
    locals()[name] = Color(*defaults[name])

    # Make backgrounds
    name_bg = name + '_bg'
    locals()[name_bg] = Color(*defaults[name], as_background=True)
    __all__.append(name_bg)
