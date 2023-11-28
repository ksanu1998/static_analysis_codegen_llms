def checkJumbled(num):
    # Convert the number to a string
    num_str = str(num)
    # Sort the characters in the string
    sorted_chars = "".join(sorted(num_str))
    # Check if the sorted string is equal to the original string
    return sorted_chars == num_str
