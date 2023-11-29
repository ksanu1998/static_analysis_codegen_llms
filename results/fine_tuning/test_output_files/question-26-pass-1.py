def findAandB(n, k):
    if (n < 10):
        print("No solution")
        return
    n = n - 1
    for (i = 1; i <= 9; i++)
        if (i!= k):
            j = n - i
            if (j >= 0):
                if (j == 0):
                    print(i, " ", i)
                else:
                    findAandB(j, i)


if __name__ == "__main__":
    n = 15
    k = 3
    findAandB(n, k)
