import numpy as np
SIZE = 3
N = 3


def minSum(A, B, C, i, n, curr, dp):
    if (n <= 0):
        return 0
    if (dp[n][curr] != -1):
        return dp[n][curr]
    if (curr == 0):
        dp[n][curr] = min(
            B[i] +
            minSum(
                A,
                B,
                C,
                i +
                1,
                n -
                1,
                1,
                dp),
            C[i] +
            minSum(
                A,
                B,
                C,
                i +
                1,
                n -
                1,
                2,
                dp))
        return dp[n][curr]
    if (curr == 1):
        dp[n][curr] = min(
            A[i] +
            minSum(
                A,
                B,
                C,
                i +
                1,
                n -
                1,
                0,
                dp),
            C[i] +
            minSum(
                A,
                B,
                C,
                i +
                1,
                n -
                1,
                2,
                dp))
        return dp[n][curr]
    dp[n][curr] = min(
        A[i] +
        minSum(
            A,
            B,
            C,
            i +
            1,
            n -
            1,
            0,
            dp),
        B[i] +
        minSum(
            A,
            B,
            C,
            i +
            1,
            n -
            1,
            1,
            dp))
    return dp[n][curr]


if __name__ == "__main__":
    A = [1, 50, 1]
    B = [50, 50, 50]
    C = [50, 50, 50]
    dp = np .zeros((SIZE, N))
    for i in range(SIZE):
        for j in range(N):
            dp[i][j] = -1
    print(min(A[0] +
              minSum(A, B, C, 1, SIZE -
                     1, 0, dp), min(B[0] +
                                    minSum(A, B, C, 1, SIZE -
                                           1, 1, dp), C[0] +
                                    minSum(A, B, C, 1, SIZE -
                                           1, 2, dp))))
