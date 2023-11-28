def spellsCount(num):
    count = 0
    for i in range(1, num + 1):
        count += len(set(str(i)))
    return count
