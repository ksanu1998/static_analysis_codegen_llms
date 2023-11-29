def createSets(N):
    if (N == 1):
        print("No solution")
        return
    GCD = 1
    for i in range(1, N):
        GCD = gcd(GCD, (i + 1) + (N - i))
    if (GCD == 1):
        print("No solution")
    else:
        print("Yes")


if __name__ == "__main__":
    N = 4
    createSets(N)
