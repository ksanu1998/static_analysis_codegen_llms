# Count the nodes in the given tree whose weight is a powerful number. 
graph = [[]for i in range(100)]
weight = [0] * 100
ans = 0


def isPowerful(n): 
    global ans
    if n == 1: 
        return True
    if weight[n] == 0: 
        weight[n] = 1
        for i in graph[n]: 
            if isPowerful(i): 
                weight[n] += weight[i] 
    return weight[n] >= n 


def dfs(n, parent): 
    global ans
    if n == 1: 
        return
    for i in graph[n]: 
        if i!= parent: 
            dfs(i, n) 
    ans += isPowerful(n) 


def solve(n, edges): 
    global ans
    ans = 0
    for i in range(n): 
        graph[i + 1].append(edges[i][0]) 
        graph[i + 1].append(edges[i][1]) 
    dfs(1, -1) 
    return ans 


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(solve(n, edges))


















































































































































