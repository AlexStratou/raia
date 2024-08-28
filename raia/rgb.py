# -*- coding: utf-8 -*-
"""
Created on Thu Aug 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com
Licence: MIT
 
Module with class definitions of all the Formatter objects.
"""
import warnings
# Definitions for the RGB codes.
CSI = '\033['
END = 'm'
FORE = '38;'
BACK = '48;'
RESET = '\033[0m'
RGB = '2;'

styles = {
    # styles map
    "bold": '1',
    "dim": '2',
    "italic": '3',
    "underline": '4',
    "blink": '5',
    "inverse": '7',
    "hidden": '8',
    "strikethrough": '9',
}

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


class Formatter(object):
    """ Class that formats strings. It is meant to be used as a parent class for
    Style and Color classes. """

    def __init__(self, format_str: str):
        """
        Initializer method of the Formater object.

        Args:
            format_str (str): The the formatting ANSI-Truecolor code

        Returns:
            None.

        """
        self.FORMATTER = format_str

    def __call__(self, text: str) -> str:
        """
        Call method for Formatter objects. It concatentates an input string with
        the formating string.

        Args:
            text (str): Text to be formatted.

        Returns:
           form_str (str): Formatted string

        """
        form_str = self.FORMATTER + text + RESET
        return form_str

    def fprint(self, *args, **kwargs):
        """
        Formated print method. Formats and prints the input using the builtin print 
        method.

        Args:
            *args (Any): Arguments for the builtin print function
            **kwargs (str): Key-word arguments for the builtin print function.

        Returns:
            None.

        """
        print(self.FORMATTER, end='')
        print(*args, **kwargs)
        print(RESET, end='')


class Style(Formatter):
    """Text style Formatter class."""

    def __init__(self, *args: str):
        """
        Initializer of the Style class. It uses the input to initialize the Formatter
        parent class.

        Args:
            *args (str): Keywords for styles, as defined on rea.rgb.styles.keys().

        Returns:
            None.

        """

        formatter = CSI
        for i, st in enumerate(args):

            if st not in styles:
                # Check if the key is valid.
                warnings.warn(
                    st +
                    ' is not a valid style key. This argument will be ignored. The valid keys are '
                    + str([*styles]))

            if i == 0:
                deli = ''  # to not include ';' on the first style code.
            else:
                deli = ';'
            formatter += deli + styles.get(st, '')
        formatter += END
        super().__init__(format_str=formatter)


class Color(Formatter):
    """ Text color Formatter class."""

    def __init__(self, Red: int, Green: int, Blue: int, as_background: bool = False):
        """
        Initializer method of the Color object. It uses the input to initialize the Formatter
        parent class. Input is in RGB code.

        Args:
            Red (int): Amount of red. Must be in [0,255]
            Green (int): Amount of red. Must be in [0,255]
            Blue (int): Amount of red. Must be in [0,255]
            as_background (bool, optional): Setting True makes the Formatter apply on the background.
            Defaults to False, i.e. the Formatter formatting the foreground.

        Raises:
            ValueError: When the RGB input is outside [0,255]
            TypeError: When RGB or is_background are not ints or bool respectively.

        Returns:
            None.

        """
        # Examine the input first.
        GOT_VALID_RGB_TYPES = isinstance(Red, int) and isinstance(
            Green, int) and isinstance(Blue, int)
        if GOT_VALID_RGB_TYPES:
            # check if the valuea are in [0,255]
            GOT_VALID_RGB_VALUES = Red >= 0 and Red <= 255 and Green >= 0 and Green <= 255 \
                and Blue >= 0 and Blue <= 255
        else:
            # if non valid type ->
            GOT_VALID_RGB_VALUES = False
        GOT_VALID_BG = isinstance(as_background, bool)
        # Is all valid:
        GOT_VALID_INPUT = GOT_VALID_RGB_TYPES and GOT_VALID_RGB_VALUES and GOT_VALID_BG

        if GOT_VALID_INPUT == True:
            # proceed to create the Formatter
            self.is_background = as_background
            self.r = str(Red)
            self.g = str(Green)
            self.b = str(Blue)

            if self.is_background == False:
                WHERE = FORE
            else:
                WHERE = BACK

            formatter = CSI + WHERE + RGB + self.r+';'+self.g+';'+self.b+END
            super().__init__(format_str=formatter)
        else:
            # Errors and warnings.
            if not GOT_VALID_RGB_TYPES:
                # meaning the RGB part is invalid.
                raise TypeError(
                    "Red, Green and Blue only take integer values in [0,255] but, types " +
                    str((type(Red), type(Green), type(Blue))) + ' were given')
            elif not GOT_VALID_RGB_VALUES:
                raise ValueError("Red, Green and Blue only take integer values in [0,255] but, values "
                                 + str((Red, Green, Blue)) + " were given.")

            else:
                raise TypeError('as_background must be type bool but, type '
                                + str(type(as_background)) + ' was given')


class FullStyle(Formatter):
    """Class that combines Color, background Color and Style Formatters"""

    def __init__(self, foreground: Color | tuple[int, int, int] = None,
                 background: Color | tuple[int, int, int] = None, style: Style | tuple[str] | str = None):
        """
        Initializer of the FullStyle Formatter.

        Args:
            foreground (Color | tuple[int, int, int]): The foreground color. The input can either be
            a rea.rgb.Color object or an iterable with the 3 RGB codes.
            background (Color | tuple[int, int, int]): The background color. The input can either be
            a rea.rgb.Color(as_background=True) object or an iterable with the 3 RGB codes.
            style (Style | tuple[str] | str): The style. The input can be either a rea.rgb.Style object or
            an iterable containing keys from rea.rgb.styles.keys(). If a single key is given, it needs not be in a tuple.

        Raises:
            ValueError: When the input cannot be interpreted.

        Returns:
            None.

        """

        if isinstance(foreground, Color):
            fore_format = foreground.FORMATTER
        elif foreground == None:
            fore_format = ''
        elif isinstance(foreground, (list, tuple)) and len(foreground) == 3:
            fore_format = Color(*foreground).FORMATTER

        else:
            raise ValueError("foreground must be a rea.Color object or an iterable of 3 integers.\
                             However, type: " + str(type(foreground))) + ' was given.'

        if isinstance(background, Color) and background.is_background:
            back_format = background.FORMATTER
        elif background == None:
            back_format = ''
        elif isinstance(background, (list, tuple)) and len(background) == 3:
            back_format = Color(*background, as_background=True).FORMATTER

        else:
            raise ValueError("background must be a rea.Color object with is_background ==True, or an iterable of 3 integers.\
                             However, type: " + str(type(background))) + ' was given.'

        if isinstance(style, Style):
            style_format = style.FORMATTER
        elif style == None:
            style_format = ''
        elif isinstance(style,  (str, tuple)):
            if isinstance(style, str):
                style_format = Style(style).FORMATTER
            else:
                # unpack if tuple (v0.2)
                style_format = Style(*style).FORMATTER

        else:
            raise ValueError("style must be a rea.Style object or an iterable of styles's keywords.\
                             However, type: " + str(type(style)) + ' was given.')

        full_format = fore_format+back_format+style_format
        super().__init__(format_str=full_format)


# what to include with * import of the file
__all__ = ['Formatter', 'Color', 'Style', 'FullStyle', 'styles', 'defaults']
