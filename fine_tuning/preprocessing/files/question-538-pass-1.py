MAX = 26


def canBeMadeEqual(str1, str2):
    # Initialize a counter for each character in str1
    count = [0] * MAX

    # Increment the count for each character in str1
    for c in str1:
        count[ord(c) - ord('a')] += 1

    # Decrement the count for each character in str2
    for c in str2:
        count[ord(c) - ord('a')] -= 1

    # Return True if all counts are zero, otherwise return False
    return all(count[i] == 0 for i in range(MAX))
