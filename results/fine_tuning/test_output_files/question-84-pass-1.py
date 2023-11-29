import sys


def kthNonDivisible(N, K):
    if (N == 1):
        print(K)
        sys.exit(0)
    if (K == 1):
        print(1)
        sys.exit(0)
    K = K - 1
    for i in range(1, N):
        if (i % N!= 0):
            K = kthNonDivisible(N, K)
            print(i)
            sys.exit(0)


if __name__ == "__main__":
    N = 10
    K = 3
    kthNonDivisible(N, K)
