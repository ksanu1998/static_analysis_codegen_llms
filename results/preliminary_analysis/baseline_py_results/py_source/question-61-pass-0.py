# Check if N is a Balanced Prime number or not. 
def isPrime(n): 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
    return True

def isBalancedPrime(n): 
    if (isPrime(n) == False): 
        return False
    if (n == 2): 
        return True
    if (n == 3): 
        return True
    if (n == 5): 
        return True
    if (n == 7): 
        return True
    if (n == 11): 
        return True
    if (n == 13): 
        return True
    if (n == 17): 
        return True
    if (n == 19): 
        return True
    if (n == 23): 
        return True
    if (n == 29): 
        return True
    if (n == 31): 
        return True
    if (n == 37): 
        return True
    if (n == 41): 
        return True
    if (n == 43): 
        return True
    if (n == 47): 
        return True
    if (n == 53): 
        return True
    if (n == 59): 
        return True
    if (n == 61): 
        return True
    if (n == 67): 
        return True
    if (n == 71): 
        return True
    if (n == 73): 
        return True
    if (n == 79): 
        return True
    if (n == 83): 
        return True