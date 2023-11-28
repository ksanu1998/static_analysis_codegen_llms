def newString(s):
    # Split the string into a list of individual characters
    chars = list(s)
    # Reverse the order of the characters in the list
    chars.reverse()
    # Join the reversed characters into a string
    new_s = "".join(chars)
    return new_s
