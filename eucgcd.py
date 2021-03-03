#!/usr/bin/python

import sys

if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    r = a % b
    print('GCD({},{})'.format(a, b))

    while r:
        a = b
        b = r
        r = a % b
        print('GCD({},{})'.format(a, b))
    print('GCD =', b)
else:
    print("\n\nUsage:   <a_number> <b_number>\n")
