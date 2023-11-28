from math import log2


def findAandB(N):
    K = int(log2(N))
    B = (1 << K)
    A = B ^ N
    print(A, B)


if __name__ == '__main__':
    N = 26
    findAandB(N)
