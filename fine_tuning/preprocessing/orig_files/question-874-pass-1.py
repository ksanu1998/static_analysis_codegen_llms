def trickyCase(s, index):
    index1 = -1
    for i in range(index - 1, -1, -1):
        digit = s[i] - '0'
        if (digit != 8):
            index1 = i
            break
    if (index1 == -1):
        return 2 * pow(10, len(s))
    num = 0
    for i in range(index1):
        num = num * 10 + (s[i] - '0')
    if (s[index1] % 2 == 0):
        num = num * 10 + (s[index1] - '0' + 2)
    else:
        num = num * 10 + (s[index1] - '0' + 1)
    for i in range(index1 + 1, len(s)):
        num = num * 10
    return num


def smallestNumber(n):
    num = 0
    s = ""
    duplicate = n
    while (n):
        s = chr(n % 10 + 48) + s
        n = int(n / 10)
    index = -1
    for i in range(len(s)):
        digit = ord(s[i]) - ord('0')
        if (digit & 1):
            index = i
            break
    if (index == -1):
        return duplicate
    if (s[index] == '9'):
        num = trickyCase(s, index)
        return num
    for i in range(index):
        num = num * 10 + ord(s[i]) - ord('0')
    num = num * 10 + (ord(s[index]) - ord('0') + 1)
    for i in range(index + 1, len(s)):
        num = num * 10
    return num


N = 2397
print(smallestNumber(N))
