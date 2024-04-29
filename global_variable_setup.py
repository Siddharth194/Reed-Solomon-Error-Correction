import gmpy2

class Global_Variables:
    def __init__(self,nu,M):
        self.M = M
        self.nu = nu
        self.k = int(gmpy2.log2(self.M))
        self.pi_array = []
        self.size = 0
