N = 8
MATRIX = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]


def knows(a, b):
    return MATRIX[a][b]


def findPotentialCelebrity(n):
    if (n == 0):
        return 0
    id_ = findPotentialCelebrity(n - 1)
    if (id_ == -1):
        return n - 1
    elif knows(id_, n - 1):
        return n - 1
    elif knows(n - 1, id_):
        return id_
    return -1


def Celebrity(n):
    id_ = findPotentialCelebrity(n)
    if (id_ == -1):
        return id_
    else:
        c1 = 0
        c2 = 0
        for i in range(n):
            if (i != id_):
                c1 += knows(id_, i)
                c2 += knows(i, id_)
        if (c1 == 0 and c2 == n - 1):
            return id_
        return -1


if __name__ == '__main__':
    n = 4
    id_ = Celebrity(n)
    if id_ == -1:
        print("No celebrity")
    else:
        print("Celebrity ID", id_)
