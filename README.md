[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI version](https://badge.fury.io/py/raia.svg)](https://badge.fury.io/py/raia)
# Raia
Simplistic python package to print colored and/or styled text with a user friendly API.

## 1. Introduction
raia is a simplistic python package that intends to provide a user friendly API for printing formatted text on the terminal. To do so, raia uses ANSI RGB codes (as many similar packages do). Truecolor ANSI support of the running terminal is assumed.

## 2. Installation
Using pip,

```bash
pip install raia
```

## 3. Usage
raia formats text through Formatter objects. All Formatter objects have two ways to format text:
1. Used as a callable, i.e.
   ```python
    form = raia.Formatter("""some initialization""")
    formatted_str = form ("raia Library")
    print(formatted_str)
    ```
2. Using the fprint method that uses the builting print with the chosen formatting, i.e.
   ```python
   form = raia.Formatter("""some initialization""")
   form.fprint("raia Library")
   ```
Both of these have the same output (printed "raia Library" with the formatting specified in """some initialization""").

The Formatter object is initialized by a string  of the ANSI escape code for the chosen formating, e.g. for printing red text we would initialize with:
```python
Red = raia.Formatter("\x1b[38;2;255;0;0m")
```
To bereft the user of having anything to do with such codes, raia provides the Style, Color, FullStyle subclasses of the Formatter class. With them, the user just has to specify the necessary information (e.g. for Color the amounts of RGB, see example below).

## 4. example.py
Below, you can see the code and output of the script example.py. 
```python
import raia

# Info
print("Package name: "+raia.__name__)
print("Version: " + raia.__version__)

# Default colors
print(raia.Red("Default 'Red' as foreground"))
print(raia.Blue_bg("Default 'Blue' as background"))

# Custom color
myColor = raia.Color(0, 150, 150)
print(myColor("Custom foreground color"))

# Custom background
myBackground = raia.Color(255, 0, 150, as_background=True)
myBackground.fprint('This is a custom background color')

# Custom style
myStyle = raia.Style(('underline', 'italic', 'bold'))
myStyle.fprint('This is custom style.')

# Custom Full-Style
myFullStyle = raia.FullStyle(foreground=raia.Violet, background=(
    0, 80, 180),                           style=myStyle)
myFullStyle.fprint('This is a custom fully styled text.')

# Default keys
print(raia.Green('Default color keys: \n'), raia.defaults.keys())
print(raia.Brown_bg('Available styles keys:\n'), raia.styles.keys())
```
Output:

<img width="580" alt="image" src="https://github.com/user-attachments/assets/ac304761-98d5-4446-acda-7d3df64e47f8">



**Important Note**: Not all styles work on all consoles.
