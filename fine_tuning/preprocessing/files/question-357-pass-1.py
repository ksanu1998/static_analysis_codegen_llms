def get_max_splits(num_string):
    # Convert the input string to an integer
    num = int(num_string)

    # Initialize a list to store the possible splits
    splits = []

    # Loop through the range of the input number
    for i in range(num, 0, -1):
        # Check if the current number is divisible by 3
        if num % i == 0:
            # Add the current number to the list of splits
            splits.append(i)

    # Return the list of splits
    return splits
