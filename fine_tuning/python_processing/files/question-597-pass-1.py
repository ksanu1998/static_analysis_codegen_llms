def countWays(s):
    # Initialize a dictionary to store the number of ways to split the string
    ways = {}

    # Loop through each character in the string
    for i in range(len(s)):
        # Get the current character
        curr_char = s[i]

        # If the current character is not in the dictionary, add it and set the value to 1
        if curr_char not in ways:
            ways[curr_char] = 1
        # Otherwise, increment the value by 1
        else:
            ways[curr_char] += 1

    # Return the number of ways to split the string
    return ways
