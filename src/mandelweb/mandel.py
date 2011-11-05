'''
Created on 5 nov 2011

@author: Legogris
'''

import numpy as np
import png
import palette
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

def isInSet(c, maxIterations):
    iterations = 0
    z = 0
    while(iterations < maxIterations):
        z = z*z + c
        if abs(z) > 2:
            return iterations
        iterations += 1
    return False

def generateSet(startPoint, endPoint, resolution):
    rows = []
    for x in np.linspace(startPoint.x, endPoint.x, resolution):
        row = []
        rows.append(row)
        for y in np.linspace(startPoint.y, endPoint.y, resolution):
            c = complex(x, y)
            n = isInSet(c, 100) % len(palette.palette)
            row.append(n)
    return rows

f = open('mandel.png', 'wb')
res = 8000
w = png.Writer(res, res, palette=palette.palette)
rows = generateSet(Point(-2, -2), Point(2, 2), res)
w.write(f, rows)
f.close()
print "finished!"