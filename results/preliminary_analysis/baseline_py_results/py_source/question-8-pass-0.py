# Maximize first array element by performing given operations at most K times. 
def getMax(arr, N, K): 
    # Initialize result 
    res = 0
    # Initialize count of operations 
    count = 0
    # Sort the array in increasing order 
    arr.sort() 
    # Traverse the array from left to right 
    for i in range(N): 
        # If the current element is smaller than the previous 
        # element, then increment the count of operations 
        if arr[i] < arr[i - 1]: 
            count += 1
        # If the count of operations exceeds K, then return 
        # the result 
        if count > K: 
            return res 
        # Update the result 
        res = max(res, arr[i]) 
    # Return the result 
    return res 
  
# Driver code 
arr = [1, 2, 3, 4, 5] 
N = len(arr) 
K = 2
print("Maximum element in the array is", getMax(arr, N, K)) 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by Rajat Mishra 

# This code is contributed by