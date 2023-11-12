# Program to check if N is a Tetradecagonal Number. 
import math


def istetradecagonal(N): 
    if (N % 2 == 0): 
        return False
    else: 
        return (math.sqrt(13*N + 1) % 1 == 0) 


# Driver Code 
if __name__ == '__main__': 
    N = 1234567890 
    if (istetradecagonal(N)): 
        print("Yes") 
    else: 
        print("No") 


# Output:
# Yes

# Explanation:
# 1234567890 is a Tetradecagonal Number.

# Time Complexity: O(1)
# Space Complexity: O(1)
