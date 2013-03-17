#!/usr/bin/env  python
__license__   = 'GPL v3'
__copyright__ = '2013, Tomasz Dlugosz <tomek3d@gmail.com>'

import os

for recipe in os.listdir('.'):
    if recipe.endswith('.recipe'):
        file = os.path.join( 'icons/' + recipe.replace('.recipe','.png'))
        if not os.path.isfile(file):
            print "no icon for " + recipe + "!"

for icon in os.listdir('icons'):
    if icon.endswith('.png'):
        file = icon.replace('.png','.recipe')
        if not os.path.isfile(file):
            print "no recipe for " + icon + "!"
    else:
        print "file " + icon + " is not an icon?"

