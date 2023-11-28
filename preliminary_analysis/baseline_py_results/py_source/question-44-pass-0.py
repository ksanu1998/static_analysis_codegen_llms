# Digitally balanced numbers. 
def checkSame(n, b): 
    if n == 0: 
        return True
    if n < 0: 
        return False
    if n % b == 0: 
        return False
    return checkSame(n // b, b) 
  
# Driver Code 
n = 1234567890 
b = 10
print(checkSame(n, b)) 
  
# This code is contributed by Nikhil Kumar Singh 