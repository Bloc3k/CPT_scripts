#!/usr/bin/python

import sys
import random
from math import gcd


def ferm_test(n):

    a = 0
    while gcd(a, n) != 1:
        a = random.randint(2, n-2)
    if pow(a, n-1, n) != 1:
        print("a={}:   {} != 1 mod {}".format(a, pow(a, n-1, n), n))
        print("{} is NOT a prime number!!!".format(n))
        sys.exit()
    else:
        print("a={}:   {} = 1 mod {}".format(a, pow(a, n-1, n), n))
        print("{} probably is a prime number".format(n))


n = int(sys.argv[1])

if len(sys.argv) == 3:
    print("\n\n")
    for i in range(int(sys.argv[2])):
        ferm_test(n)
    print("\n")
elif len(sys.argv) == 2:
    print("\n\n")
    ferm_test(n)
    print("\n")


