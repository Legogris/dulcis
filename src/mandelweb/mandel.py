'''
Created on 5 nov 2011

@author: Legogris
'''

import numpy as np
import png
import palette
import collections

Almond = collections.namedtuple('Almond', ['re', 'im', 'iterations', 'resultRe', 'resultIm', 'outside'])

def calculateAlmond(c, maxIterations):
    iterations = 0
    z = 0
    while(iterations < maxIterations):
        z = z*z + c
        if abs(z) > 2:
            return iterations
        iterations += 1
    return False

def generateSet(start, end, resolution, iterations):
    almonds = []
    for re in np.linspace(start.real, end.real, resolution):
        for im in np.linspace(start.imag, end.imag, resolution):
            c = complex(re, im)
            a = calculateAlmond(c, iterations)
            almonds.append(a)
    return almonds

def test():
    f = open('mandel.png', 'wb')
    res = 8000
    w = png.Writer(res, res, palette=palette.palette)
    rows = generateSet(complex(-2, -2), complex(2, 2), res)
    w.write(f, rows)
    f.close()
    print "finished!"