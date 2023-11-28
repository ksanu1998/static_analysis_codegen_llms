def getMaxOccurringChar(input_string):
    char_count = {}
    max_count = 0
    max_char = ""
    for char in input_string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
    return max_char
