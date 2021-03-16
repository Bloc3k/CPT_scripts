#!/usr/bin/python

import sys
from functions import possible_squares


if len(sys.argv) == 2:
    modulo = int(sys.argv[1])
    possible_squares = possible_squares(modulo)
    print('\nPosible squares: {}'.format(possible_squares))
else:
    print("\nUsage:    possibleSquares.py <modulo> ")