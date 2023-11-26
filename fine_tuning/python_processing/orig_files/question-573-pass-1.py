def maxFreq(s, a, b):
    fre = [0 for i in range(10)]
    n = len(s)
    if (a > b):
        swap(a, b)
    for i in range(0, n, 1):
        a = ord(s[i]) - ord('0')
        fre[a] += 1
    if (fre[a] == 0 and fre[b] == 0):
        return -1
    elif (fre[a] >= fre[b]):
        return a
    else:
        return b


if __name__ == '__main__':
    a = 4
    b = 7
    s = "47744"
    print(maxFreq(s, a, b))
