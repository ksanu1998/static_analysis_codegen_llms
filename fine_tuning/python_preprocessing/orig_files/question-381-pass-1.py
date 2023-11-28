MAX = 100


def check(i, add, n, k, a, dp):
    if add <= 0:
        return False
    if i >= n:
        if add == k:
            return True
        return False
    if dp[i][add] != -1:
        return dp[i][add]
    dp[i][add] = (
        check(
            i + 1,
            add - 2 * a[i],
            n,
            k,
            a,
            dp) or check(
            i + 1,
            add,
            n,
            k,
            a,
            dp))
    dp[i][add] = (check(i + 1, add - (i + 1), n, k, a, dp) or dp[i][add])
    dp[i][add] = (check(i + 1, add + i + 1, n, k, a, dp) or dp[i][add])
    return dp[i][add]


def wrapper(n, k, a):
    add = 0
    for i in range(n):
        add += a[i]
    dp = [-1] * MAX
    for i in range(MAX):
        dp[i] = [-1] * MAX
    return check(0, add, n, k, a, dp)


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    n = 4
    k = 5
    print("Yes")if wrapper(n, k, a)else print("No")
