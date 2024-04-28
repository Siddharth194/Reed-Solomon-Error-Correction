import random
import basic_ops.modulo as modulo
from basic_ops.power import *
import pickle
import copy

def Transmit(ai_array):
    with open("global_vars.bin", "rb+") as file:
        global_variables = pickle.load(file)

    k_corrupted = global_variables.nu * global_variables.k                           # number of indexes that get corrupted during transmission
    corr_indexes = random.sample(range(0, global_variables.k), int(k_corrupted))     # picking the corrupted indexes at random
    # print(corr_indexes)
    bi_array = copy.deepcopy(ai_array)

    for i in corr_indexes:
        while (bi_array[i] ==  ai_array[i]):
            bi_array[i] = random.randint(1, global_variables.pi_array[i])
    
    print(bi_array)

    with open("channel.bin","wb+") as file:
        pickle.dump(bi_array,file)


