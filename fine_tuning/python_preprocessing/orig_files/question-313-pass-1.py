dp = [[-1 for j in range(500)]for i in range(500)]


def CountSets(x, pos):
    if (x <= 0):
        if (pos == 0):
            return 1
        else:
            return 0
    if (pos == 0):
        return 1
    if (dp[x][pos] != -1):
        return dp[x][pos]
    answer = (CountSets(x - 1, pos) + CountSets(x - 2, pos - 1))
    dp[x][pos] = answer
    return answer


def CountOrderedSets(n):
    factorial = [0 for i in range(10000)]
    factorial[0] = 1
    for i in range(1, 10000):
        factorial[i] = factorial[i - 1] * i
    answer = 0
    for i in range(1, n + 1):
        sets = CountSets(n, i) * factorial[i]
        answer = answer + sets
    return answer


if __name__ == "__main__":
    N = 3
    print(CountOrderedSets(N))
