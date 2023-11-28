N = 8
MATRIX = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]


def knows(a, b):
    return MATRIX[a][b]


def findCelebrity(n):
    indegree = [0 for x in range(n)]
    outdegree = [0 for x in range(n)]
    for i in range(n):
        for j in range(n):
            x = knows(i, j)
            outdegree[i] += x
            indegree[j] += x
    for i in range(n):
        if (indegree[i] == n - 1 and outdegree[i] == 0):
            return i
    return -1


if __name__ == '__main__':
    n = 4
    id_ = findCelebrity(n)
    if id_ == -1:
        print("No celebrity")
    else:
        print("Celebrity ID", id_)
