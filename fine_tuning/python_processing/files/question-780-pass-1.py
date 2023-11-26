def countSubsequences(A):
    # Initialize result with 0
    result = 0

    # Loop through all elements in A
    for i in range(len(A)):
        # Get the current element and its bitwise XOR with the previous element
        curr_xor = A[i] ^ (A[i-1] if i > 0 else 0)

        # If the bitwise XOR is odd, increment the result
        if curr_xor % 2 == 1:
            result += 1

    # Return the result
    return result
