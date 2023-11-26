def max_balanced_prefix(str, n):
    # Initialize variables
    max_len = 0
    start = 0
    end = 0

    # Iterate through the string
    for i in range(n):
        # Check if the current character is a left parentheses
        if str[i] == "(":
            # Increment the start index
            start += 1
        # Check if the current character is a right parentheses
        elif str[i] == ")":
            # Decrement the end index
            end -= 1
        # Check if the current character is a balanced parentheses
        if start == end:
            # Update the maximum length
            max_len = max(max_len, end - start + 1)

    # Return the maximum length
    return max_len
