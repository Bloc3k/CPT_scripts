#!/usr/bin/python

import sys
import random
import functions

if len(sys.argv) == 3:
    g = int(sys.argv[1])
    modulo = int(sys.argv[2])
    phi = functions.phi_func(modulo)
    divisors = functions.find_divisors(phi)
    elem = functions.elem(modulo)[1]

    if elem.__contains__(g):
        print('\nphi({}) = {}'.format(modulo, phi))
        print('Z*{}: {}'.format(str(modulo), elem))
        print('Possible elements orders: {}'.format(divisors))

        print('g = {}:'.format(g))
        for i in range(phi):
            if pow(g, i + 1, modulo) == 1:
                print('   {}^{} = {} = 1   <--  {} is NOT a generator'.format(g, i + 1, pow(g, i + 1, modulo), g))
                sys.exit()
            else:
                if i + 1 == phi:
                    print('   {}^{} = {} != 1   <--  {} is a generator'.format(g, i + 1, pow(g, i + 1, modulo), g))
                else:
                    print('   {}^{} = {} != 1'.format(g, i + 1, pow(g, i + 1, modulo)))
    else:
        print('\ng = {} is NOT an element in Z*{}!!!   COMPUTATION CANT BE DONE!!!!!'.format(g, modulo))
else:
    print('\nBAD arguments!!!')
    print('Usage:   gen.py <element> <modulo>')
