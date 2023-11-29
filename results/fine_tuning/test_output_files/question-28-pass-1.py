def maxLCMWithGivenSum(X):
    n = 1
    while (n <= X):
        if (X % n == 0):
            if (X / n == n):
                print(n)
                break
            else:
                print(n * (X / n))
                break
        n += 1


if __name__ == "__main__":
    maxLCMWithGivenSum(10)
