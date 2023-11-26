def MaxPrefix(string):
    # Initialize variables
    max_prefix = ""
    current_prefix = ""
    frequency = {}

    # Loop through each character in the string
    for char in string:
        # If the character is not in the frequency dictionary, add it and set its frequency to 1
        if char not in frequency:
            frequency[char] = 1
        # If the character is already in the frequency dictionary, increment its frequency
        else:
            frequency[char] += 1

        # If the frequency of the character is greater than or equal to the length of the current prefix,
        # update the current prefix to the maximum length prefix that ends with this character
        if frequency[char] >= len(current_prefix):
            current_prefix = max_prefix

        # Add the character to the current prefix
        current_prefix += char

        # Update the maximum prefix
        max_prefix = max(max_prefix, current_prefix)

    return max_prefix
