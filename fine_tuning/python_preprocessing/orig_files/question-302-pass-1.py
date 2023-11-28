def calculateSum(n):
    return (2 * (n * (n + 1) * (2 * n + 1) // 6) + n * (n + 1) // 2 + 2 * (n))


if __name__ == "__main__":
    n = 3
    print("Sum =", calculateSum(n))
