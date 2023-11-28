def countReduce(str):
    n = len(str)
    res = 0
    for i in range(0, int(n / 2)):
        res += abs(int(ord(str[i])) - int(ord(str[n - i - 1])))
    return res


str = "abcd"
print(countReduce(str))
