# Tetradic Primes. 
def isContaindigit(n): 
    for i in range(2, n): 
        if n % i == 0: 
            return False
    return True

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

def isTetradicPrime(n): 
    if isPrime(n) == False: 
        return False
    if isContaindigit(n) == False: 
        return False
    return True

def tetradicPrimes(n): 
    for i in range(2, n): 
        if isTetradicPrime(i) == True: 
            print(i)

tetradicPrimes(100)