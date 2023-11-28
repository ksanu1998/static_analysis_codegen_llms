n = 3
dp = [[0 for i in range(n)]for j in range(n)]


def answerQueries(queries, q):
    for i in range(q):
        x1, y1, x2, y2 = queries[i]
        max_a = 0
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if dp[i][j] > max_a:
                    max_a = dp[i][j]
        print(max_a)
