graph = [[]for i in range(100)]
weight = [0] * 100
ans = 0


def isPowerful(n):
    if (weight[n] == 1)
        return 1
    if (weight[n] == 0)
        return 0
    for i in range(n):
        if (graph[n][i] == 1):
            if (isPowerful(i) == 1):
                ans += 1
    weight[n] = ans
    return ans


n = 10
graph[1][2] = 1
graph[1][3] = 1
graph[2][4] = 1
graph[3][4] = 1
graph[4][5] = 1
graph[5][6] = 1
graph[6][7] = 1
graph[7][8] = 1
graph[8][9] = 1
graph[9][10] = 1
isPowerful(1)
print(weight[1])
