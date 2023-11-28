# Chocolate Distribution Problem. 
def minChocolates(A, N): 
    # Sort the array in increasing order 
    A.sort() 
  
    # Initialize result 
    result = 0
  
    # Traverse the array from left to right 
    for i in range(N): 
        # If the difference between current 
        # element and next element is 1, 
        # then add 1 to result 
        if (A[i] - A[i - 1] == 1): 
            result += 1
  
    # Return the result 
    return result 
  
# Driver Code 
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
N = len(A) 
print("Minimum number of chocolates are", 
      minChocolates(A, N)) 