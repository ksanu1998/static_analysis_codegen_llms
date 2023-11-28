def findNthOccur(string, ch, N):
    count = 0
    for i in range(len(string)):
        if string[i] == ch:
            count += 1
        if count == N:
            return i
    return -1
