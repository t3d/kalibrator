#!/usr/bin/env  python
__license__   = 'GPL v3'
__copyright__ = '2013, Tomasz Dlugosz <tomek3d@gmail.com>'

import os

www_recipes=[]
tv_stations=[]
for recipe in os.listdir('.'):
    if recipe.endswith('.recipe'):
        if not recipe.startswith('tv_'):
            www_recipes += [recipe]
        else:
            tv_stations += [recipe]

www_recipes.sort()
for recipe in www_recipes:
    for line in open(recipe):
        if 'description' in line:
            if line[-2] == '"':
               desc = line.split('"')[1]
            else:
               desc = line.split('\'')[1]
            if '\\' in desc:
                desc = unicode(desc,'unicode-escape')
            print '*',recipe,'-', desc
            break
print
print '### Program stacji telewizyjnych'
tv_stations.sort()
for recipe in tv_stations:
    print '*',recipe

