V = 4
answer = []


def tsp(graph, v, currPos, n, count, cost):
    if count == n:
        return cost
    for i in range(v):
        if i not in currPos:
            newCurrPos = currPos[:]
            newCurrPos.append(i)
            newCost = cost + graph[currPos[-1]][i]
            tsp(graph, v, newCurrPos, n, count + 1, newCost)
