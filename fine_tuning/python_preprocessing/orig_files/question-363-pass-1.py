n = 3
dp = [[0 for i in range(n)]for j in range(n)]


def answerQueries(queries, q):
    for i in range(q):
        x = queries[i][0]
        x -= 1
        y = queries[i][1]
        y -= 1
        print(dp[x][y])


def pre_compute(a):
    if a[0][0] == 'a':
        dp[0][0] = 0
    else:
        dp[0][0] = 1
    for row in range(n):
        for col in range(n):
            if (row != 0 or col != 0):
                dp[row][col] = 9999
            if (row != 0):
                dp[row][col] = min(dp[row][col], dp[row - 1][col])
            if (col != 0):
                dp[row][col] = min(dp[row][col], dp[row][col - 1])
            if (a[row][col] != 'a' and (row != 0 or col != 0)):
                dp[row][col] += 1


if __name__ == '__main__':
    a = [('a', 'b', 'a'), ('a', 'c', 'd'), ('b', 'a', 'b')]
    queries = [(1, 3), (3, 3)]
    q = 2
    pre_compute(a)
    answerQueries(queries, q)
