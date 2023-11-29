N = 100005
mod = (int)(1e9 + 7)
factorial = [0] * N
modinverse = [0] * N


def power(a, m1):
    if m1 == 0:
        return 1
    else:
        return a * power(a, m1 - 1) % m1


def solve(arr):
    global N, mod, factorial, modinverse
    for i in range(N):
        factorial[i] = factorial[i - 1] * (i % mod) % mod
        modinverse[i] = power(factorial[i], mod - 2)

    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        for j in range(i, N):
            dp[j + 1] = (dp[j + 1] + dp[j - i] * arr[i] % mod * modinverse[i]) % mod
    return dp[N]


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(solve(arr))
