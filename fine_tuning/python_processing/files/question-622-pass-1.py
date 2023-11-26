MAX_CHAR = 26


def checkCorrectOrNot(s):
    # Convert the string to a list of characters
    char_list = list(s)

    # Split the list into two halves
    first_half = char_list[:len(char_list) // 2]
    second_half = char_list[len(char_list) // 2:]

    # Create a set of characters for each half
    first_half_set = set(first_half)
    second_half_set = set(second_half)

    # Check if the sets are equal
    return first_half_set == second_half_set
