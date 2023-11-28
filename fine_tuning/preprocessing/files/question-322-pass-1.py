import sys
inf = sys .maxsize


def bellman(s, d, ed, n):
    dist = [inf] * n
    dist[s] = 0
    for i in range(n):
        for u, v, w in ed:
            if dist[u]!= inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist[d]
