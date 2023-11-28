def charactersCount(str, n):
    count = 0
    for i in range(len(str)):
        if str[i] == 'a':
            count += 1
    return count
