# Minimum row or column swaps required to make every pair of adjacent cell of a Binary Matrix distinct. 
def minSwaps(b): 
    n = len(b) 
    # Create a 2D array to store the number of swaps 
    # required to make every pair of adjacent cell 
    # distinct. 
    dp = [[0 for i in range(n)] for j in range(n)] 
  
    # Fill the table using the above recursive formula 
    for gap in range(1, n): 
        for i in range(n - gap): 
            j = i + gap 
            if b[i] == b[j]: 
                dp[i][j] = dp[i + 1][j - 1] + 1
            else: 
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
  
    # Return the minimum number of swaps required 
    return dp[0][n - 1] 
  
# Driver program to test above function 
b = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 