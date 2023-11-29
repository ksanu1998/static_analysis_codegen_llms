def computePrime(N):
    count = 0
    for i in range(2, N+1):
        if isPrime(i):
            count += 1
    return count

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True