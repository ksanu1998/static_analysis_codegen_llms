N = 3


def solve(v):
    res = []
    all3 = v[0] + v[1] + v[2]
    res .append(all3 - v[1] * 2)
    res .append(all3 - v[2] * 2)
    res .append(all3 - v[0] * 2)
    return res


def findVertex(xmid, ymid):
    V1 = solve(xmid)
    V2 = solve(ymid)
    for i in range(0, 3):
        print(V1[i], end=" ")
        print(V2[i])


if __name__ == '__main__':
    xmid = [5, 4, 5]
    ymid = [3, 4, 5]
    findVertex(xmid, ymid)
