import numpy as np
n = 3
dp = np .zeros((n, n, 2))
v = np .zeros((n, n, 2))


def max_three(a, b, c):# Write your code here
    return max(a, b, c)


def max_two(a, b):[/INST]
    # Write your code here
    return max(a, b)


def max_one(a):[/INST]
    # Write your code here
    return a


def solve(i, j, k):[/INST]
    # Write your code here
    if i == n - 1 and j == n - 1 and k == n - 1:
        return v[i][j][k]
    else:
        return max(solve(i + 1, j, k), solve(i, j + 1, k), solve(i, j, k + 1))


def main():[/INST]
    # Write your code here
    for i in range(n):
        for j in range(n):
            for k in range(n):
                v[i][j][k] = max_three(dp[i][j][0], dp[i][j][1], dp[i][j][2])
    print(solve(0, 0, 0))


if __name__ == "__main__":
    main()
