dp = [[-1 for j in range(500)]for i in range(500)]


def CountSets(x, pos):
    if pos == len(x):
        return 1
    if dp[pos][x[pos]]!= -1:
        return dp[pos][x[pos]]
    count = 0
    for i in range(pos, len(x)):
        if x[i] - x[pos] > 1:
            count += CountSets(x, i + 1)
    dp[pos][x[pos]] = count
    return count
