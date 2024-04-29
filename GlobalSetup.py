import MillerRabin
import random
import gmpy2
from global_variable_setup import *
import pickle


def GlobalSetup(nu,M):
    global_vars = Global_Variables(nu,M)

    print('Printing primes:')
    while True:                         # generation of the array of k primes, p1, p2, ..., pk
        k = random.randint(1,3000)
        if (MillerRabin.MillerRabin(k) and k not in global_vars.pi_array):
            print(k)
            global_vars.pi_array.append(k)
            global_vars.size += 1

        else:
            continue

        if global_vars.size == global_vars.k:
            break

    # Save global_vars object to a binary file
    with open("global_vars.bin", "wb") as file:
        pickle.dump(global_vars, file)
