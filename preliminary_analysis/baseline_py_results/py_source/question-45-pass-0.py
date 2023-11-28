# Sum of series formed by difference between product and sum of N natural numbers. 
def seriesSum(n): 
    return (n * (n + 1) * (2 * n + 1)) / 6 
  
# Driver code 
n = 10
print("Sum of series formed by difference between product and sum of N natural numbers is: ", 
      seriesSum(n)) 

# Output:
# Sum of series formed by difference between product and sum of N natural numbers is:  220

# Time Complexity: O(1)
# Space Complexity: O(1)