import gmpy2
def modulo(dividend, divisor):
    negative_result = False
    if dividend < 0:
        dividend = abs(dividend)
        negative_result = True
    if divisor < 0:
        divisor = abs(divisor)

    original_divisor = divisor

    while (divisor << 1) <= dividend:
        divisor <<= 1
    
    rem = dividend

    while rem >= original_divisor:
        if divisor <= rem:
            rem -= divisor
        
        divisor >>= 1
    
    if negative_result:
        rem = -rem
    
    if rem < 0:
        rem = divisor + rem
    
    return rem

print(modulo(-34,15))