def Kmultiples(n, k):
    print(n * (k & (k - 1)))


if __name__ == "__main__":
    n = 2
    k = 4
    Kmultiples(n, k)
