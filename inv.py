#!/usr/bin/python

import sys

if len(sys.argv) == 3:
    try:
        inv = pow(int(sys.argv[1]), -1, int(sys.argv[2]))
    except ValueError:
        print("\nThe element {} mod {} does NOT have inverse!!!".format(sys.argv[1], sys.argv[2]))
        sys.exit()

    print("\nInverse to {} mod {} is {}".format(sys.argv[1], sys.argv[2], inv))
elif len(sys.argv) == 2 and (sys.argv[1] == '-t' or sys.argv[1] == '--theory'):
    print('\n-------------------------------------- THEORY - INVERSE --------------------------------------------')
    print('Inverse a^(-1) such that:     a*a^(-1) = 1(mod n)')
    print('Inverse exist ONLY if a and n are comprime, means GCD(a,n) = 1 !!!')
    print('----------------------------------------------------------------------------------------------------')
else:
    print('\nUsage:     inv.py <element> <modulo>')
    print('           inv.py <-t | --theory>')
