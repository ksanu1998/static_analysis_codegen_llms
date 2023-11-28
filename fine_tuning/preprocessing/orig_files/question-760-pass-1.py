def floorDifference(A, N, X):
    totalSum = 0
    perElementSum = 0
    for i in range(N):
        totalSum += A[i]
        perElementSum += A[i] // X
    totalFloorSum = totalSum // X
    return abs(totalFloorSum - perElementSum)


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    X = 4
    N = len(A)
    print(floorDifference(A, N, X))
