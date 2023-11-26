inf = 100000000


def smPath(s, d, ed, n, k):
    dist = [[inf for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        dist[i][0] = ed[s][i]
    for j in range(1, k+1):
        for i in range(n):
            for u in range(n):
                if dist[u][j-1]!= inf and ed[u][i]!= inf:
                    dist[i][j] = min(dist[i][j], dist[u][j-1] + ed[u][i])
    return dist[d][k]
