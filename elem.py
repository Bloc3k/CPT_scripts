#!/usr/bin/python

import sys
from math import gcd

z = int(sys.argv[1])
elem_addit = []
elem_multi = []

for i in range(z):
    elem_addit.append(i)

for i in range(z):
    if gcd(z, i) == 1:
        elem_multi.append(i)

print("Elements of an additive group Z" + str(z) + ": " + str(elem_addit))
print("Elements of a multiplicative group Z" + str(z) + ": " + str(elem_multi))

