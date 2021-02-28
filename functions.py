from math import gcd, sqrt


def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if gcd(x, y) == 1]
        return len(n)


def elem(x):
    elem_addit = []
    elem_multi = []

    for i in range(x):
        elem_addit.append(i)

    for i in range(x):
        if gcd(x, i) == 1:
            elem_multi.append(i)
    return elem_addit, elem_multi


def factorization(n):
    fact = []
    i = 2
    while i <= n:
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    return fact


def find_divisors(n):
    divisors = []
    i = 1
    while i <= n:
        if (n % i==0):
            divisors.append(i)
        i = i + 1
    return divisors


def elem_order(e, modulo):
    if elem(modulo).__contains__(e):
        i = 1
        while pow(e, i, modulo) != 1:
            i += 1
        return i
    else:
        print('{} is NOT an element of a Z*{}'.format(e, modulo))
