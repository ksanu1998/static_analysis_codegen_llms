def maximum_pallindromic(arr):
    # Initialize variables to store the maximum number of palindromic strings of length 3
    # and the actual palindromic strings
    max_count = 0
    palindromic_strings = []

    # Iterate over the given array of alphabets
    for i in range(len(arr)):
        # Check if the current alphabet is a palindrome
        if arr[i] == arr[i][::-1]:
            # If it is a palindrome, increment the count of palindromic strings
            max_count += 1
            # Add the current alphabet to the list of palindromic strings
            palindromic_strings.append(arr[i])

    # Return the maximum number of palindromic strings of length 3 and the list of palindromic strings
    return max_count, palindromic_strings
