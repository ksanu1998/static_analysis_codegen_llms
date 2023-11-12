# Giuga Numbers. 
import math


def isComposite(n): 
    if n <= 1: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            return True
    return False

def isPrime(n): 
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while(i * i <= n): 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i = i + 6
    return True