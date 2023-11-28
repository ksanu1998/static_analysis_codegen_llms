def lexoString(s, k):
    # Create a list of characters from the input string
    char_list = list(s)

    # Find the index of the character at position k in the list
    i = char_list.index(s[k])

    # Check if the character at position k is the last character in the list
    if i == len(char_list) - 1:
        # If it is, return an empty string
        return ""
    else:
        # If it's not, find the index of the next greater character
        j = char_list.index(s[k + 1], i + 1)

        # Return the substring of the input string starting from position j to the end of the string
        return s[j:]
