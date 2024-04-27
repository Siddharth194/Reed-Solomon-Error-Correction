import gmpy2
from . import modulo

# def mul(a, b):
#     result = 0
#     while b > 0:
#         if modulo.modulo(b,2):
#             result += a
#         a <<= 1
#         b >>= 1
#     return result

# def karatsuba(x, y):
#     if x < 10 or y < 10:
#         return x * y

#     n = max(len(str(x)), len(str(y)))
#     half_n = n >> 1

#     a, b = divmod(x, 10**half_n)
#     c, d = divmod(y, 10**half_n)

#     ac = karatsuba(a, c)
#     bd = karatsuba(b, d)
#     ad_bc = karatsuba((a + b), (c + d)) - ac - bd

#     # Combine the results using the formula
#     return (10**(2*half_n)) * ac + (10**half_n) * ad_bc + bd

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