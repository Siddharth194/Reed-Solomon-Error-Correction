import random
import basic_ops.modulo as modulo
from basic_ops.power import *
import pickle

with open("global_vars.bin", "rb+") as file:
    global_variables = pickle.load(file)

k_corrupted = global_variables.nu * global_variables.k

corr_indexes = random.sample(range(0, global_variables.k), k_corrupted)