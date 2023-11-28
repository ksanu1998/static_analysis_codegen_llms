def minOperations(A, n):

def minOperations(A, n):
    # Initialize the minimum number of operations to 0
    min_operations = 0
    # Loop through the array and count the number of 1s
    count = 0
    for i in range(n):
        if A[i] == 1:
            count += 1
    # If the number of 1s is odd, we need to flip the last 0
    if count % 2 == 1:
        min_operations += 1
    # If the number of 1s is even, we need to flip the last 1
    else:
        min_operations += 2
    return min_operations
