import numpy as np
import sys
RODS = 3
N = 3
dp = np .zeros((N + 1, RODS + 1, RODS + 1))


def initialize():
    for i in range(N + 1):
        for j in range(1, RODS + 1):
            for k in range(1, RODS + 1):
                dp[i][j][k] = sys .maxsize


def mincost(idx, src, dest, costs):
    if (idx > N):
        return 0
    if (dp[idx][src][dest] != sys .maxsize):
        return dp[idx][src][dest]
    rem = 6 - (src + dest)
    ans = sys .maxsize
    case1 = costs[src - 1][dest - 1] + \
        mincost(idx + 1, src, rem, costs) + mincost(idx + 1, rem, dest, costs)
    case2 = (costs[src - 1][rem - 1] + mincost(idx + 1,
                                               src,
                                               dest,
                                               costs) + mincost(idx + 1,
                                                                dest,
                                                                src,
                                                                costs) + costs[rem - 1][dest - 1] + mincost(idx + 1,
                                                                                                            src,
                                                                                                            dest,
                                                                                                            costs))
    ans = min(case1, case2)
    dp[idx][src][dest] = ans
    return ans


if __name__ == "__main__":
    costs = [[0, 1, 2], [2, 0, 1], [3, 2, 0]]
    initialize()
    print(mincost(1, 1, 3, costs))
