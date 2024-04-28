import gmpy2
import random
import pickle
import basic_ops.modulo as modulo
from basic_ops.power import *

with open("global_vars.bin", "rb+") as file:
    global_variables = pickle.load(file)

with open("channel.bin","rb+") as file:
    received_arr = pickle.load(file)

    