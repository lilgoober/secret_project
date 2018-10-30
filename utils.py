import math

def secretFunction():
    print('Secret function called!')
    return list(math.erf(x/10) for x in range(10))
