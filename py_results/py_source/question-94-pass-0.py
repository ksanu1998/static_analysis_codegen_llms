# Nth positive number whose absolute difference of adjacent digits is at most 1. 
def findNthNumber(N): 
    # Base case 
    if N == 1: 
        return 1 
  
    # Initialize result 
    result = 1 
  
    # Initialize count 
    count = 1 
  
    # Iterate while count is less than N 
    while count < N: 
        # Increment result by 1 
        result += 1 
  
        # Initialize count to 1 
        count = 1 
  
        # Iterate while result is not a valid number 
        while not isValid(result): 
            # Increment count 
            count += 1
  
            # Increment result by 1 
            result += 1
  
    # Return result 
    return result 
  
# Driver Code 
N = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000