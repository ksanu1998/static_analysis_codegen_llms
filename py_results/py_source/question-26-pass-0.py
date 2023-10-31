# Find two numbers whose sum is N and does not contain any digit as K. 
def findAandB(n, k): 
    # Initialize two variables 
    a = 0
    b = n 
  
    # Keep subtracting k from b until b is smaller than a 
    while b >= a: 
        if (n - a) % b == 0: 
            return a, b 
        a += 1
        b -= 1
  
    return -1, -1
  
# Driver code 
n = 100
k = 20
print(findAandB(n, k)) 

# Output: 
# (20, 80)

# Time Complexity: O(n)
# Space Complexity: O(1)