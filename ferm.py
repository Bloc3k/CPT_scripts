#!/usr/bin/python

import sys
import random
from math import gcd


def ferm_test(n):
    if n == 4:
        print('4 is NOT a prime number')
        return
    if n == 3:
        print('3 is a prime number')
        return
    if n == 2:
        print('2 is a prime number')
        return

    a = 0
    while gcd(a, n) != 1:
        a = random.randint(2, n-2)
    if pow(a, n-1, n) != 1:
        print("a={}:   {} != 1 mod {}".format(a, pow(a, n-1, n), n))
        print("{} is NOT a prime number!!!\n".format(n))
        sys.exit()
    else:
        print("a={}:   {} = 1 mod {}".format(a, pow(a, n-1, n), n))
        print("{} probably is a prime number\n".format(n))


if len(sys.argv) == 3:
    print("\n\n")
    for i in range(int(sys.argv[2])):
        if i > 100000:
            print("\nUuuuuuhh that's hard bruh, I need rest  :C")
            print("So i am saying It is Prime with 10000000% probability and go fuck of man...")
            sys.exit()
        ferm_test(int(sys.argv[1]))
    print("\n")
elif len(sys.argv) == 2:
    print("\n\n")
    ferm_test(int(sys.argv[1]))
    print("\n")
else:
    print("\n\nUsage:    ferm.py <number_to_test>")
    print("          ferm.py <number_to_test> <n_times>\n")


