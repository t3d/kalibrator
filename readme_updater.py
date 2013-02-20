#!/usr/bin/env  python
__license__   = 'GPL v3'
__copyright__ = '2012, Tomasz Dlugosz <tomek3d@gmail.com>'

import os

tv_stations=[]
for recipe in os.listdir('.'):
    if recipe.endswith('.recipe'):
        if not recipe.startswith('tv_'):
            for line in open(recipe):
                if 'description' in line:
                   print '*',recipe,'-',line.split('\'')[1]
                   break
        else:
             tv_stations += [recipe]

for recipe in tv_stations:
    print '*',recipe

