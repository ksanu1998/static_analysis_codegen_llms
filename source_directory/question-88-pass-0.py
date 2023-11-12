# Find Prime Adam integers in the given range [ L , R ]. 
def reverse(a): 
    n = len(a) 
    for i in range(n//2): 
        a[i], a[n-i-1] = a[n-i-1], a[i] 
    return a 

def sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime 

def prime_adam_integers(L, R): 
    prime = sieve(R) 
    prime_adam_integers = [] 
    for i in range(L, R+1): 
        if (prime[i] == True): 
            prime_adam_integers.append(i) 
    return prime_adam_integers 

def main(): 
    L, R = map(int, input().split()) 
    prime_adam_integers = prime_adam_integers(L, R) 
    prime_adam_integers = reverse(prime_adam_integers) 
    print(*prime_adam_integers) 

if __name__ == '__main__': 
    main() 













































































































































