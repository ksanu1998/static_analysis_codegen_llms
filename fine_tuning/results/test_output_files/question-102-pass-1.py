def PythagoreanTriplet(n):
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i * i + j * j == n * n):
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    n = 12
    PythagoreanTriplet(n)
