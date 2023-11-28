def SieveOfEratosthenes(prime, n):
    for i in range(n + 1):
        prime[i] = True
    prime[0] = prime[1] = False
    i = 2
    while i * i <= n:
        if (prime[i]):
            j = 2
            while i * j <= n:
                prime[i * j] = False
                j += 1
        i += 1


def removePrimeFrequencies(s):
    n = len(s)
    prime = [False] * (n + 1)
    SieveOfEratosthenes(prime, n)
    m = {}
    for i in range(len(s)):
        if s[i] in m:
            m[s[i]] += 1
        else:
            m[s[i]] = 1
    new_String = ""
    for i in range(len(s)):
        if (prime[m[s[i]]]):
            continue
        new_String += s[i]
    print(new_String, end="")


Str = "geeksforgeeks"
removePrimeFrequencies(list(Str))
