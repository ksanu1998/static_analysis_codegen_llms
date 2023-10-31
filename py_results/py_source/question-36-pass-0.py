# Count of ways to distribute N items among 3 people with one person receiving maximum. 
def countWays(N): 
    # Base case 
    if N <= 2: 
        return N 
  
    # Initialize result 
    result = 0 
  
    # Try all possible ways to distribute N items 
    for k in range(1, N): 
        result += countWays(k) * countWays(N - k) 
  
    return result 
  
# Driver program to test above function 
N = 5
print("Number of ways to distribute", N, 
      "items among 3 people is", countWays(N)) 