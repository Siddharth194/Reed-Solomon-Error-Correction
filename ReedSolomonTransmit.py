import random
import basic_ops.modulo as modulo
from basic_ops.power import *
import pickle

with open("global_vars.bin", "rb+") as file:
    global_variables = pickle.load(file)

k_corrupted = global_variables.nu * global_variables.k                      # number of indexes that get corrupted during transmission
corr_indexes = random.sample(range(0, global_variables.k), k_corrupted)     # picking the corrupted indexes at random

bi_array = 
for i in corr_indexes:
