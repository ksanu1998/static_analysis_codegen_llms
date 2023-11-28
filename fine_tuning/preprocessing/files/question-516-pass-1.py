def largestCharacter(str):
    largest = ""
    for char in str:
        if char > largest:
            largest = char
    return largest
