# Count all pairs of divisors of a number N whose sum is coprime with N. 
import math as m


def CountPairs(n): 
    count = 0
    for i in range(1, n): 
        if m.gcd(i, n) == 1: 
            count += 1
    return count 


# Driver code 
n = 10
print("Number of pairs of divisors of", n, "is", CountPairs(n)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)