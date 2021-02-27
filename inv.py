#!/usr/bin/python

import sys

try:
    inv = pow(int(sys.argv[1]), -1, int(sys.argv[2]))
except ValueError:
    print("The element {} mod {} does NOT have inverse !!!".format(sys.argv[1], sys.argv[2]))
    sys.exit()

print("Inverse to {} mod {} is {}".format(sys.argv[1], sys.argv[2], inv))
