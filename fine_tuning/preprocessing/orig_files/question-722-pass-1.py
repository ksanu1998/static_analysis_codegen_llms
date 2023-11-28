def isValid(arr, i, j, m, c):
    if (i == j):
        return False
    lhs = arr[j]
    rhs = m * arr[i] + c
    return (lhs == rhs)


def findOrderedPoints(arr, n, m, c):
    counter = 0
    for i in range(0, n):
        for j in range(0, n):
            firstIndex = i
            secondIndex = j
            if (isValid(arr, firstIndex, secondIndex, m, c)):
                counter = counter + 1
    return counter


arr = [1, 2, 3, 4, 2]
n = len(arr)
m = 1
c = 1
print(findOrderedPoints(arr, n, m, c))
