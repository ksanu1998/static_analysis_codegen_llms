def xorZero(str):
    # Initialize result string
    result = ""

    # Iterate over the characters of the input string
    for i in range(len(str)):
        # If the character is not '0', append it to the result string
        if str[i]!= "0":
            result += str[i]

    # Return the result string
    return result
