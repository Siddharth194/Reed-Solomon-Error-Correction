import gmpy2
import random
import basic_ops.modulo as modulo
from basic_ops.power import *

def MillerRabin(n, k = 50):

    n = gmpy2.mpz(n)

    if n == 2:
        return True

    if n < 2:
        return False

    h = 0
    d = n - 1

    while d % 2 == 0:
        h += 1
        d = d >> 1

    for i in range(k):
        a = random.randint(2, n - 1)
        x = modulo.modulo(power(a, d),n)
        if x == 1 or x == n - 1:
            continue
        for j in range(h - 1):
            x = modulo.modulo(power(x, 2),n)
            if x == n - 1:
                break
        else:
            return False
    return True
