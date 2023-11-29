def prime(n):
    if (n == 1):
        return 0
    for (i in range(2, int(n / 2) + 1)):
        if (n % i == 0):
            return 0
    return 1


if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    if (prime(a + b + c)):
        print("Yes")
    else:
        print("No")
