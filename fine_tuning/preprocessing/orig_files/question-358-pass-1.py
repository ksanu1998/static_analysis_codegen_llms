M = 20
dp = []
d, K = None, None


def count(pos, cnt, tight, nonz, num: list):
    if pos == len(num):
        if cnt == K:
            return 1
        return 0
    if dp[pos][cnt][tight][nonz] != -1:
        return dp[pos][cnt][tight][nonz]
    ans = 0
    limit = 9 if tight else num[pos]
    for dig in range(limit + 1):
        currCnt = cnt
        if dig == d:
            if d != 0 or not d and nonz:
                currCnt += 1
        currTight = tight
        if dig < num[pos]:
            currTight = 1
        ans += count(pos + 1, currCnt, currTight, (nonz or dig != 0), num)
    dp[pos][cnt][tight][nonz] = ans
    return dp[pos][cnt][tight][nonz]


def solve(x):
    global dp, K, d
    num = []
    while x:
        num .append(x % 10)
        x //= 10
    num .reverse()
    dp = [[[[-1, -1]for i in range(2)]for j in range(M)]for k in range(M)]
    return count(0, 0, 0, 0, num)


if __name__ == "__main__":
    L = 11
    R = 100
    d = 2
    K = 1
    print(solve(R) - solve(L - 1))
