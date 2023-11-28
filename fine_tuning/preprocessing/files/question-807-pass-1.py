def dfs(tree, visit, ans, node):
    if node in visit:
        return
    visit.add(node)
    ans.append(node)
    for child in tree[node]:
        dfs(tree, visit, ans, child)
