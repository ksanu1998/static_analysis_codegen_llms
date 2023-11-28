MAX = 26


def minOperation(str, len):
    first, last = [0] * MAX, [0] * MAX
    for i in range(MAX):
        first[i] = -1
        last[i] = -1
    for i in range(len):
        index = (ord(str[i]) - ord('a'))
        if (first[index] == -1):
            first[index] = i
        last[index] = i
    minOp = -1
    for i in range(MAX):
        if (first[i] == -1 or first[i] == last[i]):
            continue
        cnt = len - (last[i] - first[i] + 1)
        if (minOp == -1 or cnt < minOp):
            minOp = cnt
    return minOp


str = "abcda"
len = len(str)
print(minOperation(str, len))
