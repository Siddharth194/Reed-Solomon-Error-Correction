import gmpy2

def division(dividend, divisor):
    original_divisor = divisor
    quotient = 0
    q = 1

    while (divisor << 1) <= dividend:
        divisor <<= 1
        q <<= 1

    rem = dividend

    while rem >= original_divisor:
        if divisor <= rem:
            rem -= divisor
            quotient += q

        divisor >>= 1
        q >>= 1

    return quotient
