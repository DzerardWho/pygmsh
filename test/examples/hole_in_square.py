#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygmsh as pg
import numpy as np

def generate():
    # Characteristic length
    lcar = 1e-1

    # Coordinates of lower-left and upper-right vertices of a square domain
    xmin = 0.0
    xmax = 5.0
    ymin = 0.0
    ymax = 5.0

    # Vertices of a square hole
    squareHoleCoordinates = np.array([[1, 1, 0],
                             [4, 1, 0],
                             [4, 4, 0],
                             [1, 4, 0]])

    # Create geometric object
    geom = pg.Geometry()

    # Create square hole
    squareHole = [geom.add_polygon_loop(squareHoleCoordinates, lcar)]

    # Create square domain with square hole
    geom.add_rectangle(xmin, xmax, ymin, ymax, 0.0, lcar, holes=squareHole)

    # Return geo-file code
    return geom.get_code()

if __name__ == '__main__':
    print(generate())
