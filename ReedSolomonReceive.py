import gmpy2
import random
import pickle
import basic_ops.modulo as modulo
from basic_ops.power import *

from CRT import resolve_crt
from EGCD_a_b import *
from EEA import *
from Thues import *

#Reading the global variables.
with open("global_vars.bin", "rb+") as file:
    global_variables = pickle.load(file)

#Redaing the corrupted sequence.
with open("channel.bin","rb+") as file:
    received_arr = pickle.load(file)

#Generating the solution 'b' such that b is congruent to bi(mod pi) for all 'i' from 0 to k-1.
solution_to_corrupted_sequence,n=resolve_crt(received_arr,global_variables.pi_array)

#Generating the sequence of ri,qi,si,ti for GCD(n,b)
ri_seq,qi_seq,si_seq,ti_seq=EEA(n,solution_to_corrupted_sequence)

#Number of corrupted indices.
l=global_variables.nu * global_variables.k

#Generating P as the product of 'l' largest primes.
P=1
pi_sort=global_variables.pi_array
pi_sort.sort()
pi_sort=pi_sort[::-1]
for i in range(0,len(pi_sort)):
    if(l==0):
        break
    P=P*pi_sort[i]
    l=l-1

#Generating Values of r* and t*.
r_asterisk=global_variables.M*P
t_asterisk=P

#Applying Thues lemma to get the required r',s',t'.
r_prime,q_prime,s_prime,t_prime=Thues(ri_seq,qi_seq,si_seq,ti_seq,r_asterisk,t_asterisk)

#Checking if the message can be reconstructed and printing appropriately.
if(modulo(r_prime,t_prime)==0):
    print(division(r_prime,t_prime))
    pass
else:
    print("Error reconstructing. Can't be reconstructed")
