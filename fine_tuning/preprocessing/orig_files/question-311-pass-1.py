digits = []
vis = [False for i in range(170)]
dp = [[[[0 for l in range(170)]for k in range(2)]
       for j in range(19)]for i in range(19)]


def ConvertIntoDigit(n):
    while (n > 0):
        dig = n % 10
        digits .append(dig)
        n //= 10
    digits .reverse()


def solve(idx, k, tight, sum):
    if (idx == len(digits) and k == 0 and sum % 2 == 1):
        if (not vis[sum]):
            vis[sum] = True
            return 1
        return 0
    if (idx > len(digits)):
        return 0
    if (dp[idx][k][tight][sum]):
        return dp[idx][k][tight][sum]
    j = 0
    if (idx < len(digits) and tight == 0):
        j = digits[idx]
    else:
        j = 9
    cnt = 0
    for i in range(0 if k else 1, j + 1):
        newtight = tight
        if (i < j):
            newtight = 1
        if (i == 0):
            cnt += solve(idx + 1, k - 1, newtight, sum)
        else:
            cnt += solve(idx + 1, k, newtight, sum + i)
    dp[idx][k][tight][sum] = cnt
    return cnt


if __name__ == '__main__':
    N = 169
    k = 2
    ConvertIntoDigit(N)
    k = len(digits) - k
    print(solve(0, k, 0, 0))
