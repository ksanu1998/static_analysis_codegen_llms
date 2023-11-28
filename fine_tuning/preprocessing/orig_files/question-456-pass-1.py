def nthTerm(N):
    nth = 0
    if (N % 2 == 1):
        nth = (N * N) + 1
    else:
        nth = (N * N) - 1
    return nth


if __name__ == "__main__":
    N = 5
    print(nthTerm(N))
