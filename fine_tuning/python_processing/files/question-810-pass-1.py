def checkRedundancy(Str):
    count = 0
    for char in Str:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
    return count == 0
