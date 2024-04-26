import gmpy2
from . import modulo

def mul(a, b):
    result = 0
    while b > 0:
        if modulo.modulo(b,2):
            result += a
        a <<= 1
        b >>= 1
    return result

def power(base, exp):
    ans = 1

    while exp:
        if modulo.modulo(exp,2):
            ans = mul(ans,base)
            exp = exp - 1
        else:
            base = gmpy2.mul(base,base)
            exp = exp >> 1

    return ans

print(power(2,10))