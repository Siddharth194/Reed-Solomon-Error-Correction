import pickle
import gmpy2
import basic_ops.modulo as modulo
from basic_ops.power import *

with open("global_vars.bin", "rb+") as file:
    global_variables = pickle.load(file)

a = 235457

ai_array = []

for i in global_variables.pi_array:
    ai_array.append(modulo.modulo(a,i))
    