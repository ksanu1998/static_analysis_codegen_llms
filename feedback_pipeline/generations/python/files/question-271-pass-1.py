def minOperations(A, n):
    # Initialize variables
    min_operations = 0
    current_sum = 0

    # Iterate through the array
    for i in range(n):
        current_sum += A[i]

        # Check if the current sum is greater than the previous sum
        if current_sum > 0:
            min_operations += 1

    return min_operations