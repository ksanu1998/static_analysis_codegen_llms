import sys
import math


def maxLength(s, n):
    # Initialize a list to store the maximum length of the signal at each position
    max_length = [0] * n

    # Loop through each position in the string
    for i in range(n):
        # Check if the current position is a 1
        if s[i] == "1":
            # If it is, set the maximum length at that position to the current position
            max_length[i] = i
        else:
            # If it's not a 1, check if there is a previous 1 in the string
            for j in range(i-1, -1, -1):
                # If there is a previous 1, set the maximum length at the current position to the maximum of the current position and the previous 1
                if s[j] == "1":
                    max_length[i] = max(max_length[i], max_length[j] + 1)
                    break

    # Return the maximum length of the signal
    return max(max_length)
