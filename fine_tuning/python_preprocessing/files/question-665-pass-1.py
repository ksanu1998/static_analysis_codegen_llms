from queue import Queue


class node:
    color = 1
    edges = set()


def canPaint(nodes, n, m):
    # Create a queue to store the nodes to be colored
    queue = Queue()

    # Add the first node to the queue
    queue.put(nodes[0])

    # Loop through the nodes
    while not queue.empty():
        # Get the current node from the queue
        current = queue.get()

        # If the current node is not colored, color it
        if current.color == 0:
            current.color = 1

        # Loop through the edges of the current node
        for edge in current.edges:
            # If the edge node is not colored, add it to the queue
            if edge.color == 0:
                queue.put(edge)

    # Check if all nodes are colored
    for node in nodes:
        if node.color == 0:
            return False
    return True
