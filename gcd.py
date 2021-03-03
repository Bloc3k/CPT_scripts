#!/usr/bin/python

import sys
from math import gcd

if len(sys.argv) == 4 and sys.argv[1] == '-n':
    print(gcd(int(sys.argv[2]), int(sys.argv[3])))
elif len(sys.argv) == 3:
    print("GCD({},{}) = {}".format(sys.argv[1], sys.argv[2], str(gcd(int(sys.argv[1]), int(sys.argv[2])))))
else:
    print('\n\nUsage:    gcd.py [-n] <a_number> <b_number>\n')
