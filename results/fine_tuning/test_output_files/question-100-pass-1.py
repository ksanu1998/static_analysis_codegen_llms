from math import sqrt


def ArithmeticMean(A, B):
    return (A + B) / 2


def HarmonicMean(A, B):
    return 2 / (1 / A + 1 / B)


def find(A, B):
    n = len(A)
    for i in range(n):
        if (A[i] == B):
            return 1
    return 0


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = 10
    C = ArithmeticMean(A[0], B)
    D = HarmonicMean(A[0], B)
    if (find(A, C) and find(A, D)):
        print("Yes")
    else:
        print("No")
