import gmpy2

class Global_Variables:
    def __init__(self):
        self.M = 1000000
        self.nu = 0.2
        self.k = int(gmpy2.log2(self.M))
        self.pi_array = []
        self.size = 0