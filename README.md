[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPi](https://img.shields.io/pypi/v/raia.svg)](https://pypi.org/project/raia/)
![versions](https://img.shields.io/pypi/pyversions/raia.svg)
# Raia
Simplistic python package to print colored/styled text and emojis with a user friendly API.

## 1. Introduction
Raia is a simplistic python package that intends to provide a user friendly API for printing formatted text on the terminal. To do so, raia uses ANSI RGB codes (as many similar packages do). Truecolor ANSI support of the running terminal is assumed.

## 2. Installation
Using pip,

```bash
pip install raia
```

## 3. Usage

### 3.1 Text formatting

Raia formats text through Formatter objects. All Formatter objects have two ways to format text:
1. Used as a callable, i.e.
   ```python
    initialization = 'some initialization'
    form = raia.Formatter(initialization)
    formatted_str = form("raia package")
    print(formatted_str)
    ```
2. Using the fprint method that uses the builtin print with the chosen formatting, i.e.
   ```python
   initialization = 'some initialization'
   form = raia.Formatter(initialization)
   form.fprint("raia package")
   ```
Both of these have the same output (printed "raia package" with the formatting specified in the initialization string).

The Formatter object is initialized by a string  of the ANSI escape code for the chosen formating, e.g. for printing red text we would initialize with:
```python
Red = raia.Formatter("\x1b[38;2;255;0;0m")
```
To bereft the user of having anything to do with such codes, raia provides the Style, Color, FullStyle subclasses of the Formatter class. With them, the user just has to specify the necessary information (e.g. for Color the amounts of RGB, see example below).
```python
customBlue = raia.Color(50,150,250)
customBlue.fprint('Some blue text')
```
Output:

![image](https://github.com/user-attachments/assets/a2c53fb7-6848-422d-a437-786e1d058388)

To use a color as background, one must specify it in the initialization of the Color object as,

```python
customBlueBG = raia.Color(50,150,250, as_background=True)
customBlueBG.fprint('Some text in blue background')
```

Output:

![image](https://github.com/user-attachments/assets/50b1c895-54b8-4681-a9a1-c4684edae958)



For commonly used colors and styles, some Color and Style objects are pre-initialized and can be used out of the box.
For example,

```python
print(raia.Red('This is red.'), raia.Underline('This is undeline.'))
```
is equivalent to,
```python
Red = raia.Color(255,0,0) # or  = raia.Color('Red')
Underline = raia.Style('underline')
print(Red('This is red.'), Underline('This is undeline.'))
```
with output:

![image](https://github.com/user-attachments/assets/868e3806-2843-46a4-8136-fb5b151debba)

A full list of these default color/style keys can be found in 
```python
raia.defaults.keys() # default colors
raia.styles.keys()
```

___

### 3.2 Emojis

The emoji functionality, is implemented through Emoji objets. For example,
```python
Heart = raia.Emoji('<3')
Cookie = raia.Emoji('cookie')
print('I ' + Heart + ' ' + Cookie + '!')
```
Output:

I ❤  🍪!

A full list of currently supported emojis can be found in
```python
raia.emojis.keys()
```

For more concreate usage examples check the example.py script.

## 4. example.py
Below, you can see the code and output of the script example.py. 
```python
import raia

# Info
print("Package name: "+raia.__name__)
print("Version: " + raia.__version__)

# Default colors
print(raia.Red("Default 'Red' as foreground."))
print(raia.Blue_bg("Default 'Blue' as background."))

# Custom color
myColor = raia.Color(0, 150, 150)
print(myColor("Custom foreground color."))

# Custom background
myBackground = raia.Color(255, 0, 150, as_background=True)
myBackground.fprint('This is a custom background color.')

# Default style
print(raia.Strikethrough('This is a default style.'))

# Custom style
myStyle = raia.Style('underline', 'italic', 'bold')
myStyle.fprint('This is a custom style.')

# Custom Full-Style
myFullStyle = raia.FullStyle(foreground=raia.Violet, background=(
    0, 80, 180),                           style=myStyle)
myFullStyle.fprint('This is a custom fully styled text.')

# Default keys
print(raia.Green('Default color keys: \n'), [*raia.defaults])
print(raia.Brown_bg('Available styles keys:\n'), [*raia.styles])

# Some text with emojis
Heart = raia.Emoji('<3')
print('This prints a heart emoji: ' + Heart)

Smiley = raia.Emoji(':)')
pointRight = raia.Emoji('backhand_index_pointing_right')
print(pointRight + "Emojis and " +
      myFullStyle('Formatter objects') + ' can work together' + Smiley)


print(raia.Lime('Full list of emojis:'))
for emj_key in raia.emojis:
    tmpEmoji = raia.Emoji(emj_key)
    print(tmpEmoji, end='')
```
Output:

![image](https://github.com/user-attachments/assets/267ae979-0e96-4709-96d9-972502a04d1d)




**Important Note**: Not all styles work on all consoles.
