import pickle
import gmpy2
import basic_ops.modulo as modulo
from basic_ops.power import *
from ReedSolomonTransmit import *


def ReedSolomonSend(a):

    #Reading the global variables.
    with open("global_vars.bin", "rb+") as file:
        global_variables = pickle.load(file)

    #Generating the sequence ai defined as ai is congruent to a(mod pi).
    ai_array = []
    for i in global_variables.pi_array:
        ai_array.append(modulo.modulo(a,i))

    print('Original sequence: ',ai_array)

    #Transmitting the Sequence.
    Transmit(ai_array)
