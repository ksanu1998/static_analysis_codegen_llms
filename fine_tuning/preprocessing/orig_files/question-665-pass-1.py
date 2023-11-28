from queue import Queue


class node:
    color = 1
    edges = set()


def canPaint(nodes, n, m):
    visited = [0 for _ in range(n + 1)]
    maxColors = 1
    for _ in range(1, n + 1):
        if visited[_]:
            continue
        visited[_] = 1
        q = Queue()
        q .put(_)
        while not q .empty():
            top = q .get()
            for _ in nodes[top].edges:
                if nodes[top].color == nodes[_].color:
                    nodes[_].color += 1
                maxColors = max(
                    maxColors, max(
                        nodes[top].color, nodes[_].color))
                if maxColors > m:
                    print(maxColors)
                    return 0
                if not visited[_]:
                    visited[_] = 1
                    q .put(_)
    return 1


if __name__ == "__main__":
    n = 4
    graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    m = 3
    nodes = []
    for _ in range(n + 1):
        nodes .append(node())
    for _ in range(n):
        for __ in range(n):
            if graph[_][__]:
                nodes[_].edges .add(_)
                nodes[__].edges .add(__)
    print(canPaint(nodes, n, m))
