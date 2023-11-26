import math as mt


def find_permutation(string, k):
    # Calculate the number of permutations possible
    num_permutations = mt.factorial(len(string)) / (mt.factorial(len(string) - k) * mt.factorial(k))

    # Initialize an empty list to store the permutations
    permutations = []

    # Iterate through the possible permutations
    for i in range(num_permutations):
        # Get the current permutation as a string
        current_permutation = ''.join(sorted(string))

        # Add the permutation to the list if it has the correct length
        if len(current_permutation) == k:
            permutations.append(current_permutation)

    # Return the list of permutations
    return permutations
