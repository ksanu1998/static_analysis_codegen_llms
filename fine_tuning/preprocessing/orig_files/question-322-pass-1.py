import sys
inf = sys .maxsize


def bellman(s, d, ed, n):
    if (s == d):
        return 0
    dis = [0] * (n + 1)
    for i in range(1, n + 1):
        dis[i] = inf
    dis[s] = 1
    for i in range(n - 1):
        for it in ed:
            dis[it[1]] = min(dis[it[1]], dis[it[0]] * ed[it])
    for it in ed:
        if (dis[it[1]] > dis[it[0]] * ed[it]):
            return -2
    if (dis[d] == inf):
        return -1
    else:
        return dis[d]


if __name__ == "__main__":
    n = 3
    ed = {(1, 2): 0.5, (1, 3): 1.9, (2, 3): 3}
    s = 1
    d = 3
    get = bellman(s, d, ed, n)
    if (get == -2):
        print("Cycle Detected")
    else:
        print(get)
