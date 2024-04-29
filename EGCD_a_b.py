import gmpy2
from basic_ops import modulo, power

#Returns the ri,si,ti sequence.
def BinaryEGCD(a,b):
    orig_a = a
    orig_b = b
    e = 0
    r = int(a)
    r_prime = int(b)

    while ((modulo.modulo(r,2) == 0) and (modulo.modulo(r_prime,2) == 0) and a != 0 and b != 0):
        r = r >> 1
        r_prime = r_prime >> 1
        e = e + 1

    a = r
    b = r_prime

    s = 1
    s_prime = 0

    t = 0
    t_prime = 1

    while (r_prime != 0):
        while (modulo.modulo(r,2) == 0):
            r = r >> 1
            if (not(modulo.modulo(s,2) == 0 and modulo.modulo(t,2) == 0)):
                s = s + b
                t = t - a

            s = s >> 1
            t = t >> 1

        while (modulo.modulo(r_prime,2) == 0):
            r_prime = r_prime >> 1

            if not(modulo.modulo(s_prime,2) == 0 and modulo.modulo(t_prime,2) == 0):
                s_prime = s_prime + b
                t_prime = t_prime - a

            s_prime = s_prime >> 1
            t_prime = t_prime >> 1

        if(r > r_prime):
            r, r_prime = r_prime, r
            s, s_prime = s_prime, s
            t, t_prime = t_prime, t

        r_prime = r_prime - r
        s_prime = s_prime - s
        t_prime = t_prime - t

    return (power.power(2,e)*r,s,t)
