#!/usr/bin/python

import sys
from functions import phi_func

print("Order(Z*{}) = {}".format(sys.argv[1], phi_func(int(sys.argv[1]))))