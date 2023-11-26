def nthTerm(N):
    nth = 0
    first_term = 12
    nth = (first_term * (pow(2, N - 1))) + 11 * ((pow(2, N - 1)) - 1)
    return nth


if __name__ == "__main__":
    N = 5
    print(nthTerm(N))
