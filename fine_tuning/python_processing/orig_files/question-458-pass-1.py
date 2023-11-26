def nthTerm(N):
    nth = 0
    first_term = 4
    pi = 1
    po = 1
    n = N
    while (n > 1):
        pi *= n - 1
        n -= 1
        po *= 2
    nth = (first_term * pi) // po
    return nth


if __name__ == "__main__":
    N = 5
    print(nthTerm(N))
