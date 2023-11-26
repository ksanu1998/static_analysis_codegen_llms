def longest_subseq(n, k, s):
    # Create a dictionary to store the length of the longest subsequence
    # that ends at each index
    lengths = {}

    # Initialize the length of the longest subsequence
    max_length = 0

    # Iterate over the input array
    for i in range(n):
        # Get the current element
        element = s[i]

        # Check if the current element is present in the dictionary
        if element in lengths:
            # If it is present, increment the length of the longest subsequence
            # that ends at the current index
            lengths[element] += 1
        else:
            # If it is not present, set the length of the longest subsequence
            # that ends at the current index to 1
            lengths[element] = 1

        # Check if the length of the longest subsequence that ends at the current
        # index is greater than the maximum length
        if lengths[element] > max_length:
            # If it is, update the maximum length
            max_length = lengths[element]

    # Return the maximum length
    return max_length
