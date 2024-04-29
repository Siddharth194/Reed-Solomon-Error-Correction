import gmpy2
from basic_ops.modulo import *
from basic_ops.division import *
from EGCD_a_b import *

def resolve_crt(list_a,list_n):
    #Calculating the product of all the primes.
    n=1
    for i in list_n:
        n=n*i

    solution=0
    X=0

    #Calculating X=sigma(Xi*ai*Ni) for all 'i' from 0 to k-1 as defined in class.
    for i in range(0,len(list_a)):
        Ni=division(n,list_n[i])
        d,s,t=BinaryEGCD(Ni,list_n[i])
        X=X+(list_a[i]*s*Ni)

    #Calculate X(modn)
    solution=modulo.modulo(X,n)

    return solution,n
