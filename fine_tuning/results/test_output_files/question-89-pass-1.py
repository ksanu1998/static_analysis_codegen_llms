def sumDig(n):
    if (n == 0):
        return 0
    sum = 0
    while (n > 0):
        sum += (n % 10)
        n //= 10
    if (sum == 1):
        return 1
    else:
        return 0


if __name__ == "__main__":
    N = 1234
    if (sumDig(N)):
        print("Yes")
    else:
        print("No")
