def findMaximumNum(st, n, k):
    # Initialize a variable to store the maximum number
    max_num = 0

    # Loop through each digit of the input number
    for i in range(n):
        # Get the current digit
        digit = int(st[i])

        # If the digit is not 9, we can try changing it to 9
        if digit!= 9:
            # Create a copy of the input number
            new_num = st[:i] + str(9) + st[i+1:]

            # Recursively call the function with the new number
            max_num = max(max_num, findMaximumNum(new_num, n-1, k-1))

        # If the digit is 9, we cannot change it
        else:
            # Recursively call the function with the input number
            max_num = max(max_num, findMaximumNum(st, n-1, k))

    # Return the maximum number
    return max_num
