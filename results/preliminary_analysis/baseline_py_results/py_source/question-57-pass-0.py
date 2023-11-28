# Sum of given N fractions in reduced form. 
def gcd(a, b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
def lcm(a, b): 
    return (a * b) // gcd(a, b) 
  
# Returns the sum of N fractions in reduced form. 
def sum_of_fractions(N): 
    # Initialize result 
    result = 0
  
    # Initialize the denominator 
    den = 1
  
    # Initialize the numerator 
    num = 0
  
    # Iterate through all fractions 
    for i in range(N): 
        # Add the numerator and denominator 
        num += fractions[i][0] 
        den += fractions[i][1] 
  
    # Divide the numerator by the denominator 
    num = num // den 
  
    # Return the result 
    return num 
  
# Driver code 
N = 3
fractions = [[1, 2], [1, 3], [1, 4]] 
print(sum_of_fractions(N)) 