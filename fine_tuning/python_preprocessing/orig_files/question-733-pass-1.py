def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def getReducedForm(dy, dx):
    g = gcd(abs(dy), abs(dx))
    sign = (dy < 0) ^ (dx < 0)
    if (sign):
        return (-abs(dy) // g, abs(dx) // g)
    else:
        return (abs(dy) // g, abs(dx) // g)


def minLinesToCoverPoints(points, N, xO, yO):
    st = dict()
    minLines = 0
    for i in range(N):
        curX = points[i][0]
        curY = points[i][1]
        temp = getReducedForm(curY - yO, curX - xO)
        if (temp not in st):
            st[temp] = 1
            minLines += 1
    return minLines


xO = 1
yO = 0
points = [[-1, 3], [4, 3], [2, 1], [-1, -2], [3, -3]]
N = len(points)
print(minLinesToCoverPoints(points, N, xO, yO))
