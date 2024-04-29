import gmpy2
from . import modulo

def power(base, exp):
    ans = 1

    while exp:
        if modulo.modulo(exp,2):
            ans = ans*base
            exp = exp - 1
        else:
            base = gmpy2.mul(base,base)
            exp = exp >> 1

    return ans
