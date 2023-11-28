def smallest_lexicographic_string(s, k):
    # Sort the string in lexicographic order
    s = ''.join(sorted(s))
    # Perform the required number of operations
    for i in range(k):
        # Find the first occurrence of the character 'z' in the string
        index = s.find('z')
        # If the character 'z' is not found, the string is already in lexicographic order
        if index == -1:
            break
        # Replace the character 'z' with the next character in the alphabet
        s = s[:index] + chr(ord('a') + 1) + s[index + 1:]
    return s
