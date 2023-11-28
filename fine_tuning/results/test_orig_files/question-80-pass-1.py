def computePrime(N):

def computePrime(N):
    prime_pairs = 0
    for i in range(2, N+1):
        for j in range(i+1, N+1):
            if i % j == 0:
                prime_pairs += 1
    return prime_pairs
