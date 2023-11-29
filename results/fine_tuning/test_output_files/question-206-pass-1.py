def nthTerm(N):
    if (N == 1):
        return 1
    else:
        n = nthTerm(N - 1)
        n = n * 3
        n = n + 1
        return n


if __name__ == "__main__":
    N = 5
    print(nthTerm(N))
