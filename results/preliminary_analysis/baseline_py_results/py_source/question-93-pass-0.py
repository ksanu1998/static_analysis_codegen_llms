# Number of ways to color boundary of each block of M * N table. 
def CountWays(N, M): 
    # Base Case 
    if N == 1 or M == 1: 
        return 1
  
    # If M = 2, then only one way to color 
    # boundary of 2 * N table 
    if M == 2: 
        return N 
  
    # If N = 2, then only one way to color 
    # boundary of 2 * M table 
    if N == 2: 
        return M 
  
    # If M > 2 and N > 2, then count of ways 
    # will be sum of count of ways obtained 
    # when last row and last column is colored 
    # with different colors 
    return CountWays(N - 1, M) + CountWays(N, M - 1) 
  
# Driver Code 
N = 3
M = 4
print("Number of ways to color boundary of", 
      N, " * ", M, " table is ", 
      CountWays(N, M)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 