def findSubStringIndices(s, L):
    # Initialize result list
    result = []

    # Iterate over the words in L
    for word in L:
        # Check if the word is present in s
        if word in s:
            # Get the index of the first occurrence of the word in s
            index = s.index(word)

            # Append the index to the result list
            result.append(index)

    # Return the result list
    return result[1:]
