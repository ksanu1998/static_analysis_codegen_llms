def dfs(tree, visit, ans, node):
    num = 0
    temp = 0
    visit[node] = 1
    for i in range(len(tree[node])):
        if (visit[tree[node][i]] == 0):
            temp = dfs(tree, visit, ans, tree[node][i])
            if (temp % 2):
                num += temp
            else:
                ans[0] += 1
    return num + 1


def minEdge(tree, n):
    visit = [0] * (n + 2)
    ans = [0]
    dfs(tree, visit, ans, 1)
    return ans[0]


N = 12
n = 10
tree = [[]for i in range(n + 2)]
tree[1].append(3)
tree[3].append(1)
tree[1].append(6)
tree[6].append(1)
tree[1].append(2)
tree[2].append(1)
tree[3].append(4)
tree[4].append(3)
tree[6].append(8)
tree[8].append(6)
tree[2].append(7)
tree[7].append(2)
tree[2].append(5)
tree[5].append(2)
tree[4].append(9)
tree[9].append(4)
tree[4].append(10)
tree[10].append(4)
print(minEdge(tree, n))
