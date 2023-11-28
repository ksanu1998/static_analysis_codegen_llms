def sumOfSubstrings(num):
    # Convert the number to a string
    num_str = str(num)
    # Initialize the sum to 0
    sum = 0
    # Iterate over each character in the string
    for i in range(len(num_str)):
        # Get the substring starting from the current character
        substr = num_str[i:]
        # Convert the substring to an integer
        substr_int = int(substr)
        # Add the integer substring to the sum
        sum += substr_int
    # Return the sum
    return sum
