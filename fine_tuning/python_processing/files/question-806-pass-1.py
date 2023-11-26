def findMaxLen(string):
    max_len = 0
    start = 0
    end = 0
    for end in range(len(string)):
        if string[end] == 'a':
            max_len = max(max_len, end - start + 1)
        else:
            start = end + 1
    return max_len
