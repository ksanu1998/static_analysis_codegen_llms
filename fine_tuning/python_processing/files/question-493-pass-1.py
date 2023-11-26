def compute_hash(str):
    # Initialize the hash value to 0
    hash_value = 0
    # Loop through each character in the string
    for i in range(len(str)):
        # Get the ASCII value of the character
        char = ord(str[i])
        # Add the ASCII value to the hash value
        hash_value += char
        # Multiply the hash value by a prime number (e.g. 31)
        hash_value *= 31
    # Return the hash value
    return hash_value
