from math import gcd


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
