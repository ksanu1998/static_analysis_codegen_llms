# Sum of all numbers up to N that are co. 
def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
 
def lcm(a, b): 
    return (a * b) / gcd(a, b) 
 
# Driver program to test above function 
n = 10
print("LCM of", n, "numbers is", lcm(n)) 

# Output:
# LCM of 10 numbers is 2520

# Time Complexity: O(n)
# Space Complexity: O(1)