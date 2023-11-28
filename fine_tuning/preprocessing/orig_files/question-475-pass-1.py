def findLength(str, n):
    pre = [0] * n
    post = [0] * n
    for i in range(n):
        if (i != 0):
            pre[i] += pre[i - 1]
        if (str[i] == '1'):
            pre[i] += 1
    for i in range(n - 1, -1, -1):
        if (i != (n - 1)):
            post[i] += post[i + 1]
        if (str[i] == '0'):
            post[i] += 1
    ans = 0
    for i in range(n):
        ans = max(ans, pre[i] + post[i])
    return ans


S = "0101110110100001011"
n = len(S)
print(findLength(S, n))
