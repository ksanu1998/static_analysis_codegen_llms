import bisect


def printPosition(A, B, sizeOfA, sizeOfB):
    for i in range(sizeOfA):
        if (A[i] == B):
            print(i + 1)
            break


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = 1
    sizeOfA = len(A)
    sizeOfB = len(B)
    printPosition(A, B, sizeOfA, sizeOfB)
