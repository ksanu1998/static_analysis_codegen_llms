def print_next_vovel_string(st):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for char in st:
        if char in vowels:
            index = vowels.index(char)
            new_string += vowels[index + 1]
        else:
            new_string += char
    return new_string
