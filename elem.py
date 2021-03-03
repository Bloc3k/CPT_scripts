#!/usr/bin/python

import sys
from functions import elem

if len(sys.argv) == 2:
    z = int(sys.argv[1])
    elem_addit, elem_multi = elem(z)
    print("\n\nElements of an additive group Z{}: {}".format(z, elem_addit))
    print("Elements of a multiplicative group Z*{}: {}\n".format(z, elem_multi))
else:
    print("\n\nUsage:      elem.py <modulo>\n")

