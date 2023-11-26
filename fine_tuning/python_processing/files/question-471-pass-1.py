def isPossible(str1, str2):
    # Create a dictionary to store the count of each character in str1
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Check if all characters in str2 are present in str1
    for char in str2:
        if char not in char_count or char_count[char] <= 0:
            return False
        else:
            char_count[char] -= 1

    return True
