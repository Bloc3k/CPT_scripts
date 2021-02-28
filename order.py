#!/usr/bin/python

import sys
from functions import phi_func, elem_order

modulo = int(sys.argv[2])
e = int(sys.argv[1])

if len(sys.argv) == 2:
    print("Order(Z*{}) = {}".format(e, phi_func(e)))
elif len(sys.argv) == 3:
    if elem_order(e, modulo) == phi_func(modulo):
        print('Order of {} in Z*{}:  {}   <-- is a generator'.format(e, modulo, elem_order(e, modulo)))
    else:
        print('Order of {} in Z*{}:  {}'.format(e, modulo, elem_order(e, modulo)))
