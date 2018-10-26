import math

def secretFunction():
    return list(math.erf(x/10) for x in range(10))
