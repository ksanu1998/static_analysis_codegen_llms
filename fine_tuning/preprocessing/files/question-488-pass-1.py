def find_winner(arr, n):
    # Initialize result variable
    result = 0

    # Loop through the array of strings
    for i in range(n):
        # Check if the current string is empty
        if len(arr[i]) == 0:
            # If it is, add 1 to the result
            result += 1

    # Return the result
    return result
