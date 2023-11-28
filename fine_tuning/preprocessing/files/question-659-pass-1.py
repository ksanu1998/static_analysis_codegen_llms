N = 1000001
c = 0
n = 0
m = 0
a = 0
b = 0


def dfs(a, b, v, vis):
    vis[v] = True
    for i in range(len(graph[v])):
        if not vis[graph[v][i]] and graph[v][i]!= a and graph[v][i]!= b:
            dfs(a, b, graph[v][i], vis)
