def printNumber(holes):
    n = len(holes)
    if (n == 1):
        print(1)
        return
    holes.sort()
    print(holes[0])
    for i in range(1, n - 1):
        print(holes[i] - holes[i - 1])
    print(n + 1 - holes[n - 1])


if __name__ == "__main__":
    holes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    printNumber(holes)
