inf = 100000000


def smPath(s, d, ed, n, k):
    dis = [inf] * (n + 1)
    dis[s] = 0
    for i in range(k):
        dis1 = [inf] * (n + 1)
        for it in ed:
            dis1[it[1]] = min(dis1[it[1]], dis[it[0]] + it[2])
        for i in range(n + 1):
            dis[i] = dis1[i]
    if (dis[d] == inf):
        return -1
    else:
        return dis[d]


if __name__ == '__main__':
    n = 4
    ed = [[0, 1, 10], [0, 2, 3], [0, 3, 2], [1, 3, 7], [2, 3, 7]]
    s = 0
    d = 3
    k = 2
    print(smPath(s, d, ed, n, k))
