import math as m



def CountPairs(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            if m.gcd(i, j) == 1:
                count += 1
    return count
