def add_edge(u, v):
    global adj
    adj[u].append(v)
    adj[v].append(u)


def dfs(u, par=-1):
    global adj, parent
    parent[u] = par
    for child in adj[u]:
        if (child != par):
            dfs(child, u)


def countSmallerAncestors(n):
    global parent, adj
    dfs(1)
    for i in range(1, n + 1):
        node = i
        cnt = 0
        while (parent[node] != -1):
            if (parent[node] < i):
                cnt += 1
            node = parent[node]
        print(cnt, end=" ")


if __name__ == '__main__':
    N = 6
    adj = [[]for i in range(10 ** 5)]
    parent = [0] * (10 ** 5)
    add_edge(1, 5)
    add_edge(1, 4)
    add_edge(4, 6)
    add_edge(5, 3)
    add_edge(5, 2)
    countSmallerAncestors(N)
