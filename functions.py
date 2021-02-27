from math import gcd


def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if gcd(x, y) == 1]
        return len(n)
