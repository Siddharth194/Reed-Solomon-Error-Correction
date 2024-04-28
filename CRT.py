import gmpy2
from basic_ops.module import *

def resolve_crt(list_a,list_n):
    n=1
    for i in list_n:
        n=n*i

    solution=0
    X=0
    for i in range(0,len(list_a)):
        #Binary_EGCD(Ni,ni)
        Ni=division(n,list_n[i])
        #print('herre',Ni, 'and',list_n[i])
        d,s,t=BinaryEGCD(Ni,list_n[i])
        X=X+(list_a[i]*s*Ni)

    #Calculate Xmodn
    solution=modulo(X,n)

    return solution,n
