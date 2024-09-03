# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""
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
