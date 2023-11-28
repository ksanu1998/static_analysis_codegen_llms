mod = 1000000007
dp = [[[-1 for i in range(2)]for i in range(105)]for i in range(1005)]
powers = [0] * 1005
powersModk = [0] * 1005


def calculate(pos, rem, z, k, n):
    if (rem == 0 and z):
        if (pos != n):
            return (powers[n - pos - 1] * 9) % mod
        else:
            return 1
    if (pos == n):
        return 0
    if (dp[pos][rem][z] != -1):
        return dp[pos][rem][z]
    count = 0
    for i in range(10):
        if (i == 0):
            count = (count + (calculate(pos + 1,
                     (rem + (i * powersModk[pos]) % k) % k, z, k, n))) % mod
        else:
            count = (count + (calculate(pos + 1,
                     (rem + (i * powersModk[pos]) % k) % k, 1, k, n))) % mod
    dp[pos][rem][z] = count
    return count


def countNumbers(n, k):
    st = 1
    for i in range(n + 1):
        powers[i] = st
        st *= 10
        st %= mod
    st = 1
    for i in range(n + 1):
        powersModk[i] = st
        st *= 10
        st %= mod
    return calculate(0, 0, 0, k, n)


if __name__ == '__main__':
    N = 2
    K = 2
    print(countNumbers(N, K))
