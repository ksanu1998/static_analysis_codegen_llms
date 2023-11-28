# Length of longest subarray whose sum is not divisible by integer K. 
def MaxSubarrayLength(arr, n, k): 
    # Initialize result 
    res = 0
    # Initialize prefix sum 
    prefix_sum = 0
    # Initialize map to store prefix sum 
    # and its index 
    map = {} 
    # Traverse through the array 
    for i in range(n): 
        # Add current element to prefix sum 
        prefix_sum += arr[i] 
        # If prefix sum is divisible by k 
        if prefix_sum % k == 0: 
            # Update result 
            res = max(res, i + 1) 
        # If prefix sum is not present in map 
        if prefix_sum not in map: 
            # Add prefix sum and its index in map 
            map[prefix_sum] = i 
        else: 
            # Update result if required 
            res = max(res, i - map[prefix_sum]) 
    return res 


# Driver Code 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
n = len(arr) 
k = 5
print("Length of the longest subarray with sum divisible by k is", 
      MaxSubarrayLength(arr, n, k)) 


# This code is contributed by Rajat Mishra 
