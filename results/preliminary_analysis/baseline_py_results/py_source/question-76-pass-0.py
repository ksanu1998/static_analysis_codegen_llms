# Find the sum of the first Nth Icosagonal Numbers. 
def Icosagonal_num(n): 
    return (n*(n*n + 3*n + 2))/2

# Driver Code 
n = 10
print("Sum of first", n, "Icosagonal Numbers is", Icosagonal_num(n)) 

# Output:
# Sum of first 10 Icosagonal Numbers is 235

# Time Complexity: O(n)
# Space Complexity: O(1)