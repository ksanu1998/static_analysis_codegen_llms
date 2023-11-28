import numpy as np
import sys
MAXI = 50
INT_MAX = sys .maxsize
dp = np .ones((MAXI, MAXI, MAXI * MAXI))
dp *= -1


def minDifference(x, y, k, b, c):
    if (x >= n or y >= m):
        return INT_MAX
    if (x == n - 1 and y == m - 1):
        diff = b[x][y] - c[x][y]
        return min(abs(k - diff), abs(k + diff))
    ans = dp[x][y][k]
    if (ans != -1):
        return ans
    ans = INT_MAX
    diff = b[x][y] - c[x][y]
    ans = min(ans, minDifference(x + 1, y, abs(k + diff), b, c))
    ans = min(ans, minDifference(x, y + 1, abs(k + diff), b, c))
    ans = min(ans, minDifference(x + 1, y, abs(k - diff), b, c))
    ans = min(ans, minDifference(x, y + 1, abs(k - diff), b, c))
    return ans


if __name__ == "__main__":
    n = 2
    m = 2
    b = [[1, 4], [2, 4]]
    c = [[3, 2], [3, 1]]
    print(minDifference(0, 0, 0, b, c))
