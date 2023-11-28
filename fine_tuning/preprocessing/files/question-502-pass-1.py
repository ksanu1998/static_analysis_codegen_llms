def largestAnagramGrp(arr):
    # Create a dictionary to store the anagrams and their counts
    anagrams = {}

    # Iterate over the input array
    for word in arr:
        # Sort the word to create an anagram
        anagram = "".join(sorted(word))

        # If the anagram is already in the dictionary, increment its count
        if anagram in anagrams:
            anagrams[anagram] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            anagrams[anagram] = 1

    # Find the anagram with the largest count
    largest_anagram = max(anagrams, key=anagrams.get)

    # Return the word with the largest count
    return largest_anagram
