import sys


def maximumOccurrence(s):
    # Initialize result with 0
    result = 0

    # Create a dictionary to store the frequency of each character
    freq = {}

    # Iterate over the string
    for c in s:
        # If the character is not in the dictionary, add it and set its frequency to 1
        if c not in freq:
            freq[c] = 1
        # If the character is already in the dictionary, increment its frequency
        else:
            freq[c] += 1

    # Iterate over the dictionary and find the maximum frequency
    for key, value in freq.items():
        if value > result:
            result = value

    return result
