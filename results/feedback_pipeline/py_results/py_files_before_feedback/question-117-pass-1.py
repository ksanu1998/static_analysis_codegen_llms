def checkArray(a, b, n):
    # Initialize result
    result = 0

    # Iterate through the arrays
    for i in range(n):
        # Check if the current element in A is equal to the current element in B
        if a[i]!= b[i]:
            # If not equal, increment the result
            result += 1

    # Return the result
    return result