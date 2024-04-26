import gmpy2

def modulo(dividend, divisor):

    original_divisor = divisor

    while (divisor << 1) <= dividend:
        divisor <<= 1
    
    rem = dividend

    while rem >= original_divisor:
        if (divisor <= rem):
            rem -= divisor
        
        divisor >>= 1
    
    return rem
    

# n = gmpy2.mpz(12345)
# m = gmpy2.mpz(987)

# print(modulo(n, m))
# print(n%m)