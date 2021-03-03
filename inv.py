#!/usr/bin/python

import sys

if len(sys.argv) == 3:
    try:
        inv = pow(int(sys.argv[1]), -1, int(sys.argv[2]))
    except ValueError:
        print("\n\nThe element {} mod {} does NOT have inverse!!!".format(sys.argv[1], sys.argv[2]))
        sys.exit()

    print("\n\nInverse to {} mod {} is {}".format(sys.argv[1], sys.argv[2], inv))
else:
    print("\n\nUsage:     inv.py <element> <modulo>")
