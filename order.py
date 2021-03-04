#!/usr/bin/python

import sys
import functions


if len(sys.argv) == 2 and (sys.argv[1] == '-t' or sys.argv[1] == '--theory'):
    print("\n------------------------------------ THEORY - ORDERS ---------------------------------------")
    print('Order of a group says how many elements group has.')
    print('Order of an element says how many elements of a group can this element generate.')
    print('The only possible orders of an element are divisors of Order of a group.')
    print('Only these possible orders are necessary to test if testing an element to be a generator.')
    print('~-------------------------------------------------------------------------------------------')
elif len(sys.argv) == 2 and sys.argv[1].isnumeric():
    print('Possible elements orders: {}'.format(functions.find_divisors(functions.phi_func(int(sys.argv[1])))))
    print("Order of a group(Z*{}) = {}".format(int(sys.argv[1]), functions.phi_func(int(sys.argv[1]))))
elif len(sys.argv) == 3:
    e = int(sys.argv[1])
    modulo = int(sys.argv[2])
    print('Possible elements orders: {}'.format(functions.find_divisors(functions.phi_func(int(sys.argv[2])))))
    if functions.elem_order(e, modulo) == functions.phi_func(modulo):
        print('Order of {} in Z*{}:  {}   <-- is a generator'.format(e, modulo, functions.elem_order(e, modulo)))
    else:
        print('Order of {} in Z*{}:  {}'.format(e, modulo, functions.elem_order(e, modulo)))

else:
    print('\nUsage:   order.py <modulo>')
    print('         order.py <element> <modulo>')
    print('         order.py <-t | --theory>')
