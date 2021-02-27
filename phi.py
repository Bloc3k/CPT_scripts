#!/usr/bin/python

import sys
from functions import phi_func

print("phi({}) = {} ".format(sys.argv[1], phi_func(int(sys.argv[1]))))

