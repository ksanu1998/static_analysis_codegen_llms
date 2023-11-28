from math import sqrt


def checkPolygonWithMidpoints(arr, N, midpoints):
    for j in range(midpoints):
        val = 1
        for k in range(j, N, midpoints):
            val &= arr[k]
        if (val and N // midpoints > 2):
            print("Polygon possible with side length", (N // midpoints))
            return True
    return False


def isPolygonPossible(arr, N):
    limit = sqrt(N)
    for i in range(1, int(limit) + 1):
        if (N % i == 0):
            if (checkPolygonWithMidpoints(arr, N, i)
                    or checkPolygonWithMidpoints(arr, N, (N // i))):
                return
    print("Not possiblen")


if __name__ == "__main__":
    arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
    N = len(arr)
    isPolygonPossible(arr, N)
