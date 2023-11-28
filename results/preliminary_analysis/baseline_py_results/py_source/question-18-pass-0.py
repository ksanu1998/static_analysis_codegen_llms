# Count all distinct pairs of repeating elements from the array for every array element. 
def solve(arr, n): 
    # Create a hash table to store the count of each element 
    # and initialize the count of all elements as 0 
    count = [0] * n 
    for i in range(n): 
        count[arr[i]] += 1
    # Initialize the result 
    result = 0
    # Traverse the array 
    for i in range(n): 
        # If the count of the element is greater than 1 
        if count[arr[i]] > 1: 
            # Increment the result 
            result += 1
    return result 
  
# Driver code 
arr = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 