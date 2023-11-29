from operator import xor



def findXOR(n):
    return reduce(xor, range(n))
