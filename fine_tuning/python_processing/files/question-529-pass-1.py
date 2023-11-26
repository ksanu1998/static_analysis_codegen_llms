def countChars(string, n):
    count = 0
    for char in string:
        if char == n:
            count += 1
    return count
