m = {}


def precompute():
    m[1] = 1
    m[2] = 2
    m[3] = 6
    m[4] = 24
    m[5] = 120


def findN(n):
    if (n in m):
        return m[n]
    m[n] = findN(n - 1) + findN(n - 2)
    return m[n]


if __name__ == "__main__":
    precompute()
    n = 5
    print(findN(n))
