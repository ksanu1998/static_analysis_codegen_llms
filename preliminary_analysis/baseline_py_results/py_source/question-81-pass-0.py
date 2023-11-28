# Count of ways to write N as a sum of three numbers. 
def countWays(N): 
    # Base Case 
    if N == 0: 
        return 1
    if N < 0: 
        return 0
    return countWays(N - 1) + countWays(N - 2) + countWays(N - 3) 
  
# Driver Code 
N = 4 
print("Count of ways to write", N, "as a sum of three numbers is", countWays(N)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 