import sys


def minimumChar(S1, S2):
    # Initialize variables
    min_char = 0
    i = 0

    # Loop through each character in S1
    while i < len(S1):
        # Check if the character is present in S2
        if S1[i] in S2:
            # Increment the minimum number of characters
            min_char += 1
        i += 1

    return min_char
