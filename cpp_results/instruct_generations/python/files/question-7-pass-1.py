def isCycleExists(arr, N):
    visited = [False] * N
    stack = []
    for i in range(N):
        if not visited[i]:
            stack.append(i)
            while stack:
                node = stack.pop()
                if visited[node]:
                    return True
                visited[node] = True
                for neighbor in arr[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    return False