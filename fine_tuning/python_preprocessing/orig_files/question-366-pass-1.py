import sys
n = 3


def minFallingPathSum(A):
    for R in range(n - 2, -1, -1):
        for C in range(n):
            best = A[R + 1][C]
            if C > 0:
                best = min(best, A[R + 1][C - 1])
            if C + 1 < n:
                best = min(best, A[R + 1][C + 1])
            A[R][C] = A[R][C] + best
    ans = sys .maxsize
    for i in range(n):
        ans = min(ans, A[0][i])
    return ans


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(minFallingPathSum(A))
