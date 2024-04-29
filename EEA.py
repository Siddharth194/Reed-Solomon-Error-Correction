import gmpy2
from basic_ops.modulo import modulo
from basic_ops.division import division

def EEA(a,b):
    ri_seq=[a,b]
    si_seq=[1,0]
    ti_seq=[0,1]
    qi_seq=[0]

    i=0
    while(True):
        #quotient for r
        quotient=division(ri_seq[i],ri_seq[i+1])

        #remainder for r
        remainder=modulo(ri_seq[i],ri_seq[i+1])

        #Appending the remainder and quotient appropriately.
        ri_seq.append(remainder)
        qi_seq.append(quotient)

        #generating new s and appending appropriately.
        new_s=si_seq[i]-(quotient*si_seq[i+1])
        si_seq.append(new_s)

        #generating new t and appending appropriately.
        new_t=ti_seq[i]-(quotient*ti_seq[i+1])
        ti_seq.append(new_t)

        i=i+1

        if(remainder==0):
            break
        pass

    return ri_seq,qi_seq,si_seq,ti_seq
