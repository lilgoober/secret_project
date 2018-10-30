import math

def secretFunction():
    """Return list of 10 secret numbers"""
    print('Secret function called!')
    return [math.erf(x/10) for x in range(10))]
