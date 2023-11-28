# Print any pair of integers with sum of GCD and LCM equals to N. 
def printPair(n): 
    for i in range(1, n): 
        for j in range(i + 1, n + 1): 
            if (gcd(i, j) == n and lcm(i, j) == n): 
                print(i, j) 
  
# Driver Code 
n = 10 
printPair(n) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to find GCD of two numbers 
def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Python program to find LCM of two numbers 
def lcm(a, b): 
    return (a * b) // gcd(a, b) 
  
# Driver Code 
a = 20 
b = 15 
print("GCD of %d and %d is %d" % (a, b, gcd(a, b))) 
print("LCM of %d and %d is %d" % (a, b, lcm(a, b))) 