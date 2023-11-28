import sys


def getMinimizedSum(string, length):
    # Create a list of ASCII values for the input string
    ascii_values = [ord(char) for char in string]

    # Initialize the minimum sum to infinity
    min_sum = float('inf')

    # Iterate over all possible characters
    for char in range(length):
        # Create a new list of ASCII values by removing all occurrences of the current character
        new_ascii_values = [value for value in ascii_values if value!= char]

        # Calculate the sum of the new list of ASCII values
        sum = sum(new_ascii_values)

        # Update the minimum sum if the current sum is less than the minimum sum
        if sum < min_sum:
            min_sum = sum

    return min_sum
