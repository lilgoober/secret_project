import math

def secretFunction():
    """Return list of 10 secret numbers"""
    return list(math.erf(x/10) for x in range(10))
