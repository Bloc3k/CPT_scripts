#!/usr/bin/python

import sys
from math import gcd

print("GCD(" + str(sys.argv[1]) + ", " + str(sys.argv[2]) + ") = " + str(gcd(int(sys.argv[1]), int(sys.argv[2]))))