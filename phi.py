#!/usr/bin/python

import sys
from functions import phi_func


if len(sys.argv) > 2:
    sum = 1
    for i in range(len(sys.argv) - 1):
        sum *= int(sys.argv[i + 1])
    print("phi({}) = {} ".format(sum, phi_func(sum)))
elif len(sys.argv) == 2:
    print("phi({}) = {} ".format(sys.argv[1], phi_func(int(sys.argv[1]))))

