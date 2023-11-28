N = 1000001
c = 0
n = 0
m = 0
a = 0
b = 0


def dfs(a, b, v, vis):
    global c
    vis[a] = 1
    c += 1
    for i in v[a]:
        if (vis[i] == 0 and i != b):
            dfs(i, b, v, vis)


def Calculate(v):
    global c
    vis = [0 for i in range(n + 1)]
    c = 0
    dfs(a, b, v, vis)
    ans1 = n - c - 1
    vis = [0 for i in range(len(vis))]
    c = 0
    dfs(b, a, v, vis)
    ans2 = n - c - 1
    print(ans1 * ans2)


if __name__ == '__main__':
    n = 7
    m = 7
    a = 3
    b = 5
    edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 5]]
    v = [[]for i in range(n + 1)]
    for i in range(m):
        v[edges[i][0]].append(edges[i][1])
        v[edges[i][1]].append(edges[i][0])
    Calculate(v)
