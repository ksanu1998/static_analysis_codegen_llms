def movesRequired(a, b):
    count = 0
    while a % b!= 0:
        a -= 1
        count += 1
    return count
